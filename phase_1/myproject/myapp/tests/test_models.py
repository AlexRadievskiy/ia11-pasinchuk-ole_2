from django.test import TestCase
from phase_1.myproject.myapp.models import Passenger
from django.core.exceptions import ValidationError

class PassengerModelTests(TestCase):

    def setUp(self):
        self.passenger_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'passport_number': '12345678'
        }

    def test_create_passenger(self):
        passenger = Passenger.objects.create(**self.passenger_data)
        self.assertEqual(passenger.first_name, 'John')
        self.assertEqual(passenger.last_name, 'Doe')
        self.assertEqual(passenger.passport_number, '12345678')

    def test_passenger_string_representation(self):
        passenger = Passenger.objects.create(**self.passenger_data)
        self.assertEqual(str(passenger), 'John Doe')

    def test_invalid_passport_number(self):
        self.passenger_data['passport_number'] = ''
        with self.assertRaises(ValidationError):
            passenger = Passenger(**self.passenger_data)
            passenger.full_clean()

    def test_invalid_first_name(self):
        self.passenger_data['first_name'] = ''
        with self.assertRaises(ValidationError):
            passenger = Passenger(**self.passenger_data)
            passenger.full_clean()

    def test_invalid_date_of_birth(self):
        self.passenger_data['date_of_birth'] = 'invalid-date'
        with self.assertRaises(ValidationError):
            passenger = Passenger(**self.passenger_data)
            passenger.full_clean()
