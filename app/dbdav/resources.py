import os
import shutil
import uuid
from base64 import b64encode, b64decode
from hashlib import md5

from django.conf import settings
from django.utils.timezone import now
from djangodav.db.resources import NameLookupDBDavMixIn, BaseDBDavResource
from djangodav.fs.resources import BaseFSDavResource
from djangodav.views import DavView, RedirectFSException

from dbdav.models import CollectionModel, ObjectModel

from djangodav.auth.rest import RestAuthViewMixIn

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


def md5file(fname):
    hash_md5 = md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5


def scramble_uploaded_filename(filename):
    """ scramble/uglify the filename of the uploaded file, keep the file extension """
    if "." in filename:
        extension = filename.split(".")[-1]
        return "{}.{}".format(uuid.uuid4(), extension)
    else:
        return str(uuid.uuid4())


class AuthFsDavView(RestAuthViewMixIn, DavView):
    authentications = (BasicAuthentication(), SessionAuthentication())


class MyDBDavResource(NameLookupDBDavMixIn, BaseDBDavResource):
    collection_model = CollectionModel
    object_model = ObjectModel

    root = "/uploaded_files"

    def get_abs_path(self):
        """Return the absolute path of the resource. Used internally to interface with
        an actual file system. If you override all other methods, this one will not
        be used."""
        return os.path.join(self.root, *self.path)

    # ToDo:
    # CollectionModel needs to be Workbench Entity, e.g. Directory
    # ObjectModel needs to be the File Workbench Entity, and the File needs to be have the Directory as a parent
    # The write endpoint does not support files larger than settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    # maybe we can use the same as for multipart uploads? StreamingRequest? Or a form?
    # ToDo: the underlying library needs support for viewable() querysets


    def write(self, request, temp_file=None):
        print("Writing ... temp_file=", temp_file)

        if temp_file:
            # determine size of temp_file
            size = os.stat(temp_file).st_size

            # calculate hashsum
            hashsum = md5file(temp_file).hexdigest() # Todo: calculate hashsum (or maybe nginx can do that for us?)

            # ToDo: random_filename = scramble_uploaded_filename(self.displayname)
            random_filename = scramble_uploaded_filename(self.displayname)

            new_path = os.path.join(settings.MEDIA_ROOT, random_filename)

            shutil.move(temp_file, new_path)
        else:
            size = len(request.body)

            # calculate a hashsum of the request (ToDo: probably need to replace this with SHA1 or such, and maybe add a salt)
            hashsum = md5(request.body).hexdigest()

            # generate a random filename
            # ToDo: random_filename = scramble_uploaded_filename(self.displayname)
            random_filename = scramble_uploaded_filename(self.displayname)

            # save the file
            new_path = os.path.join(settings.MEDIA_ROOT, random_filename)

            f = open(new_path, 'wb')
            f.write(request.body)
            f.close()

        if not self.exists:
            obj = self.object_model(
                name=self.displayname,
                parent=self.get_parent().obj,
                md5=hashsum,
                size=size
            )

            obj.path.name = new_path

            obj.save()

            return

        self.obj.size = size
        self.obj.modified = now()
        self.obj.path.name = new_path
        self.obj.md5 = hashsum  # ToDo: this should be self.obj.md5 ?

        self.obj.save(update_fields=['path', 'size', 'modified', 'md5'])

    def read(self):
        return self.obj.path

    @property
    def etag(self):
        return self.obj.md5

    @property
    def getcontentlength(self):
        return self.obj.size
