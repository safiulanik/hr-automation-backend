from django.test import TestCase
from rest_framework.test import APIClient


class TestRequest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.token = ''

    def test_01_create_req(self):
        request_data = {
            'details': 'This is a demo request',
            'create_uid': 1,
            'write_uid': 1,
        }
        response = self.client.post(path='/api/v1/request/',
                                    data=request_data,
                                    HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.assertEqual(response.status_code, 200)

    def test_02_update_req(self):
        req_id = 1
        updated_request_data = {
            'details': 'This is an updated demo request',
            'create_uid': 1,
            'write_uid': 1,
        }
        response = self.client.put(path='/api/v1/request/{}'.format(req_id),
                                   data=updated_request_data,
                                   HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.assertEqual(response.status_code, 200)

    def test_03_delete_req(self):
        req_id = 1
        response = self.client.delete(path='/api/v1/request/{}'.format(req_id),
                                      HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.assertEqual(response.status_code, 200)

    def test_04_req_list(self):
        response = self.client.get(path='/api/v1/request/list/', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.assertEqual(response.status_code, 200)
