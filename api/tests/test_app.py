from unittest import TestCase
from flask import jsonify
from app import normalize, friends

import requests


class AppTest(TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:5000'
    
    def test_home(self):
        response = requests.get(self.url)

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        
    def test_healthchek(self):
        response = requests.get(f"{self.url}/healthcheck")

        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'working')

    def test_interations_errors(self):
        url = f"{self.url}/interaction"
        
        response = requests.post(url, data={"source": "Foo", "target": "Bar", "weight":6, "book": 3})
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)

        response = requests.post(url, data={"source": "Foo", "target": "Bar", "weight":6, "books": 4})
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)

        response = requests.post(url, data={"source": "Foo", "target": "Bar", "weights":6, "book": 4})
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)

        response = requests.post(url, data={"sources": "Foo", "target": "Bar", "weight":6, "book": 4})
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)

        response = requests.post(url, data={"source": "Foo", "taget": "Bar", "weight":6, "book": 4})
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)

    def test_interation(self):
        url = f"{self.url}/interaction"
        
        response = requests.post(url, data={"source": "Foo", "target": "Bar", "weight":6, "book": 4})
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 201)

    def test_common_friends_errors(self):
        url = f"{self.url}/common-friends?target=Foo&source=Bar"

        response = requests.get(url)
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'common-friends':[]})

    def test_common_friends(self):
        
        response = requests.get(f"{self.url}/common-friends?target=Foo")
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)

        response = requests.get(f"{self.url}/common-friends?source=Bar")
        self.assertFalse(response.ok)
        self.assertEqual(response.status_code, 400)
        
    def test_normalize(self):
        form = {'source':'ArYa-sTark','target':'john-SNOW'}
        normalize(form)

        self.assertEqual(form['source'], 'Arya-Stark')
        self.assertEqual(form['target'], 'John-Snow')

    def test_friends(self):
        
        result = friends([{1,2,3,4,5},{2,4,5,6}])

        self.assertIsInstance(result, set)
        self.assertEqual(result, {1,2,3,4,5,6})

    def tearDown(self):
        self.url = None