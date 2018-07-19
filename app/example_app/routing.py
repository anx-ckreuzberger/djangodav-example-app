from channels.routing import ProtocolTypeRouter

"""
Basic Routing for ASGI/Websockets

For information, please consult the django channels documentation:
- https://channels.readthedocs.io/en/latest/topics/security.html
- https://channels.readthedocs.io/en/latest/topics/routing.html
"""

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    # make sure only the hosts listed in ALLOWED_HOSTS are able to connect to the websockets
})
