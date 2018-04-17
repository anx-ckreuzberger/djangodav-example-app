from django.conf.urls import url, include

from djangodav.acls import FullAcl
from djangodav.locks import DummyLock

from fsdav.resources import MyFSDavResource, AuthFsDavView


urlpatterns = [
    # Mirroring tmp folder
    url(r'^(?P<path>.*)$', AuthFsDavView.as_view(resource_class=MyFSDavResource, lock_class=DummyLock, acl_class=FullAcl)),
]
