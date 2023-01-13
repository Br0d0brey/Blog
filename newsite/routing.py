
from channels.routing import ProtocolTypeRouter, URLRouter
import room.routing

application = ProtocolTypeRouter({
    # (http->Django views is added by default)
    'websocket':
        URLRouter(
            room.routing.websocket_urlpatterns
        ),
})