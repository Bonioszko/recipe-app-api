"""tyest for the users api"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create and return the ne user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the pulic features of the user Api.,"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful"""
        payload = {
            'email': ' test@example.com',
            'password': 'testpass123',
            "name": 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        print(1)
        self.assertNotIn('password', res.data)

    # def test_user_with_email_exists_error(self):
    #     """Check if user with email ewxist"""
    #     payload = {
    #         'email': ' test@example.com',
    #         'password': 'testpass123',
    #         "name": 'Test Name',
    #     }
    #     create_user(**payload)
    #     res = self.client.post(CREATE_USER_URL, payload)

    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_password_too_short_error(self):
    #     """Test if password is lenght enough"""
    #     payload = {
    #         'email': ' test@example.com',
    #         'password': 'pw',
    #         "name": 'Test Name',
    #     }
    #     res = self.client.post(CREATE_USER_URL, payload)

    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    #     user_exists = get_user_model().objects.filter(
    #         email=payload['email']
    #     ).exists()
    #     self.assertFalse(user_exists)
