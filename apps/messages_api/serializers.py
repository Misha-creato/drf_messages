from rest_framework import serializers

from messages_api.models import Message


class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True,
    )
    title = serializers.CharField(
        max_length=256,
        required=True,
    )
    text = serializers.CharField(
        required=False,
    )
    created_at = serializers.DateTimeField(
        read_only=True,
    )

    def create(self, validated_data):
        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        list = self.context.get('list')
        if list:
            if len(representation['text']) > 64:
                representation['text'] = representation['text'][:64] + '...'

        return representation
