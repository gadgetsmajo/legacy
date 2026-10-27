from rest_framework.test import APITestCase

from .models import Inquiry


class InquiryApiTests(APITestCase):
    def test_contact_inquiry_can_be_submitted(self):
        response = self.client.post('/api/inquiries/', {
            'kind': 'contact',
            'name': 'Coffee Customer',
            'email': 'customer@example.com',
            'subject': 'Question',
            'message': 'I would like more information.',
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Inquiry.objects.get().kind, Inquiry.Kind.CONTACT)

    def test_quote_requires_product_and_quantity(self):
        response = self.client.post('/api/inquiries/', {
            'kind': 'quote',
            'name': 'Coffee Customer',
            'email': 'customer@example.com',
            'message': 'Please send a quote.',
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Inquiry.objects.count(), 0)
