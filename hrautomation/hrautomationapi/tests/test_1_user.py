from unittest import TestCase
from rest_framework.test import APIClient


class TestUser(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_01_sign_up(self):
        user_data = {
            'first_name': 'Safiul',
            'last_name': 'Kabir',
            'email': 'safiul@{}.{}'.format('gmail', 'com'),
            'username': 'safiul@{}.{}'.format('gmail', 'com'),
            'role': 'engineer',
            'password': '12345678'
        }
        response = self.client.post(path='/api/v1/signup/', data=user_data)
        assert response.status_code == 201

    def test_02_login(self):
        login_credentials = {
            'username': 'safiul@{}.{}'.format('gmail', 'com'),
            'password': '12345678'
        }
        response = self.client.post(path='/api/v1/login/', data=login_credentials)
        assert response.status_code == 200
