from django.urls import path

from messages_api.api import (
    MessageView,
)


urlpatterns = [
    path(
        '',
        MessageView.as_view({
            'get': 'list',
            'post': 'create',
        }),
    ),
    path(
        '<str:pk>/',
        MessageView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
    ),
]
