from django.conf.urls import url, include

from djangodav.acls import FullAcl
from djangodav.locks import DummyLock

from dbdav.resources import MyDBDavResource, AuthFsDavView


urlpatterns = [
    # Mirroring tmp folder
    url(r'^(?P<path>.*)$', AuthFsDavView.as_view(resource_class=MyDBDavResource, lock_class=DummyLock, acl_class=FullAcl)),
]
