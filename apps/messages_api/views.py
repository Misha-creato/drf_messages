from django.http import (
    HttpResponseServerError,
    Http404,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from messages_api.models import Message
from messages_api.serializers import MessageSerializer


class MessageList(APIView):
    def get(self, request, format=None):
        messages = Message.objects.all()
        serializer = MessageSerializer(
            messages,
            many=True,
            context={
                'list': True,
            },
        )
        return Response(
            data=serializer.data,
        )

    def post(self, request, format=None):
        serializer = MessageSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class MessageDetail(APIView):
    def get_object(self, pk):
        try:
            message = Message.objects.filter(pk=pk).first()
        except Exception as exc:
            raise HttpResponseServerError
        if message is None:
            raise Http404
        return message

    def get(self, request, pk, format=None):
        message = self.get_object(
            pk=pk,
        )
        serializer = MessageSerializer(
            message,
        )
        return Response(
            data=serializer.data,
        )

    def put(self, request, pk, format=None):
        message = self.get_object(
            pk=pk,
        )
        serializer = MessageSerializer(
            message,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        message = self.get_object(
            pk=pk,
        )
        message.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

