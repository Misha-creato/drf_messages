from rest_framework.viewsets import ModelViewSet

from messages_api.models import Message
from messages_api.serializers import MessageSerializer


class MessageView(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
