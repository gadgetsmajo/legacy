from rest_framework.test import APITestCase

from .models import Subscriber


class NewsletterApiTests(APITestCase):
    def test_subscribe_is_idempotent(self):
        payload = {'email': 'reader@example.com'}
        self.assertEqual(self.client.post('/api/newsletter/subscribe/', payload).status_code, 201)
        self.assertEqual(self.client.post('/api/newsletter/subscribe/', payload).status_code, 201)
        self.assertEqual(Subscriber.objects.count(), 1)

    def test_unsubscribe_deactivates_subscription(self):
        Subscriber.objects.create(email='reader@example.com')
        response = self.client.post('/api/newsletter/unsubscribe/', {'email': 'reader@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Subscriber.objects.get().is_active)
