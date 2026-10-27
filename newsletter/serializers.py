from rest_framework import serializers

from .models import Subscriber

class SubscribeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        subscriber, _ = Subscriber.objects.update_or_create(
            email=validated_data['email'].lower(),
            defaults={'is_active': True, 'unsubscribed_at': None},
        )
        return subscriber
