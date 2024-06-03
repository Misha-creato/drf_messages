from django.urls import path

from messages_api.views import (
    MessageList,
    MessageDetail,
)


urlpatterns = [
    path(
        '',
        MessageList.as_view(),
    ),
    path(
        '<str:pk>/',
        MessageDetail.as_view(),
    ),
]
