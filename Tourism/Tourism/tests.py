from django.test import TestCase
from accounts.models import User


class UserModelTests(TestCase):
  def test_create_user(self):
    user = User.objects.create(username='Louis',password='1234')
    userList = User.objects.all()
    self.assertEqual(user, userList[0])
    