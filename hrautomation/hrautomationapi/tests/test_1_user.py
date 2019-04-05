from unittest import TestCase
from rest_framework.test import APIClient
from hrautomation.hrautomation.local_settings import EMAIL_DOMAIN, EMAIL_DOMAIN_EXTENSION


class TestUser(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_01_sign_up(self):
        user_data = {
            'first_name': 'Safiul',
            'last_name': 'Kabir',
            'email': 'safiul@{}.{}'.format(EMAIL_DOMAIN, EMAIL_DOMAIN_EXTENSION),
            'role': 'engineer',
            'password': '12345678'
        }
        response = self.client.post(path='/api/v1/signup/', data=user_data)
        assert response.status_code == 200

    def test_02_login(self):
        login_credentials = {
            'username': 'safiul@{}.{}'.format(EMAIL_DOMAIN, EMAIL_DOMAIN_EXTENSION),
            'password': '12345678'
        }
        response = self.client.post(path='/api/v1/login/', data=login_credentials)
        assert response.status_code == 200
