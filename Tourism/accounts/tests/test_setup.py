from rest_framework.test import APITestCase,APIClient
from django.urls import reverse

class TestSetUp(APITestCase):
  def setUp(self):
    return super().setUp()