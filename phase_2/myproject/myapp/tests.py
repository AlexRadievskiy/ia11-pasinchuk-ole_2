from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import ParentResource

class ParentResourceTests(APITestCase):
    def setUp(self):
        self.parent_resource = ParentResource.objects.create(name="Test", age=30)

    def test_create_parent_resource(self):
        url = reverse('parentresource-list')
        data = {'name': 'Test 2', 'age': 25}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_parent_resources(self):
        url = reverse('parentresource-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
