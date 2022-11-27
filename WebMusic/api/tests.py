from django.test import TestCase,Client
from django.urls import reverse #根据name reverse url
# Create your tests here.

class test_simple(TestCase):
    def setUp(self):
        self.client = Client()

    def test_getHotlist(self):
        response = self.client.get(r'/api/getHotlist')
        self.assertEqual(response.status_code,200)
        
    def test_getMusic(self):
        data = {
            'musicname':'love',
        }
        response = self.client.post(r'/api/getMusic',data)
        self.assertEqual(response.status_code,200)