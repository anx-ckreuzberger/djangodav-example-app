from django.conf.urls import url, include

from authentication.views import IsAuthenticatedViews

urlpatterns = [
    url(r'^$', IsAuthenticatedViews.as_view(), name='is-authenticated'),
]
