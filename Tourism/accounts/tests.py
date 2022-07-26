from django.test import TestCase
from accounts.models import User
from django.forms import ValidationError

class UserModelTests(TestCase):
  def test_create_user(self):
    user = User.objects.create(username='Louis',password='1234')
    userList = User.objects.all()
    self.assertEqual(user, userList[0])

  def test_incorrect_nickname(self):
    user = User(username='Louis',password='#sdfFJSD168sdf', nickname='^&^$_%#$$%^#($')
    with self.assertRaises(ValidationError):
      user.full_clean()
      user.save()

  def test_nickname_already_taken(self):
    user = User(username='Louis',password='#sdfFJSD168sdf', nickname='Louis')
    user.full_clean()
    user.save()
    user2 = User(username='Paul',password='#sdfFJSD168sdf', nickname='Louis')
    with self.assertRaises(ValidationError):
      user2.full_clean()
      user2.save()
