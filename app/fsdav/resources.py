from django.conf import settings

from djangodav.base.resources import MetaEtagMixIn
from djangodav.fs.resources import BaseFSDavResource, DummyFSDAVResource
from djangodav.views import DavView

from djangodav.auth.rest import RestAuthViewMixIn

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class AuthFsDavView(RestAuthViewMixIn, DavView):
    authentications = (BasicAuthentication(), SessionAuthentication())


class MyFSDavResource(MetaEtagMixIn, DummyFSDAVResource):
    root = settings.MEDIA_ROOT

    # def get_abs_path(self):
    #     """Return the absolute path of the resource. Used internally to interface with
    #     an actual file system. If you override all other methods, this one will not
    #     be used."""
    #     return os.path.join(self.root, *self.path)
