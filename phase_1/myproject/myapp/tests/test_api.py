from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from phase_1.myproject.myapp.models import Passenger

class PassengerAPITests(APITestCase):

    def setUp(self):
        self.passenger_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'passport_number': '12345678'
        }
        self.passenger = Passenger.objects.create(**self.passenger_data)

    def test_create_passenger(self):
        url = reverse('passenger-list')
        data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'date_of_birth': '1985-05-15',
            'passport_number': '87654321'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passenger.objects.count(), 2)
        self.assertEqual(Passenger.objects.get(id=response.data['id']).first_name, 'Jane')

    def test_get_passenger_list(self):
        url = reverse('passenger-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_passenger_detail(self):
        url = reverse('passenger-detail', args=[self.passenger.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.passenger.first_name)

    def test_update_passenger(self):
        url = reverse('passenger-detail', args=[self.passenger.id])
        data = {
            'first_name': 'UpdatedName',
            'last_name': self.passenger.last_name,
            'date_of_birth': self.passenger.date_of_birth,
            'passport_number': self.passenger.passport_number
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.passenger.refresh_from_db()
        self.assertEqual(self.passenger.first_name, 'UpdatedName')

    def test_delete_passenger(self):
        url = reverse('passenger-detail', args=[self.passenger.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Passenger.objects.count(), 0)
