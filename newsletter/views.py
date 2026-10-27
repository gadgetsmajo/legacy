from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subscriber
from .serializers import SubscribeSerializer


class SubscribeView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SubscribeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscriber = serializer.save()
        return Response(
            {'message': 'Subscription saved.', 'email': subscriber.email},
            status=status.HTTP_201_CREATED,
        )


class UnsubscribeView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not isinstance(email, str) or not email.strip():
            return Response({'email': 'A valid email address is required.'}, status=status.HTTP_400_BAD_REQUEST)
        Subscriber.objects.filter(email__iexact=email.strip(), is_active=True).update(
            is_active=False,
            unsubscribed_at=timezone.now(),
        )
        return Response({'message': 'If the address was subscribed, it has been unsubscribed.'})
