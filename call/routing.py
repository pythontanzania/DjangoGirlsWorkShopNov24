from django.urls import re_path

from . import consumers

call_websocket_urlpatterns = [
    re_path(r'ws/call/', consumers.CallConsumer.as_asgi()),
]
