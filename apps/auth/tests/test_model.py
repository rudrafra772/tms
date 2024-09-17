from django.test import TestCase
from apps.auth.models import UserModel

class UserModelTests(TestCase):
    def setUp(self):
        self.email = 'testuser@example.com'
        self.username = 'testuser'
        self.password = 'password123'

    def test_create_user(self):
        user = UserModel.objects.create_user(email = self.email, username = self.username)
        user.set_password(self.password)
        self.assertEqual(self.email, user.email)
        self.assertEqual(self.username, user.username)
        self.assertTrue(user.check_password(self.password))
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_deleted)

    def test_create_superuser(self):
        user = UserModel.objects.create_superuser(email = self.email, username = self.username)
        user.set_password(self.password)
        self.assertEqual(self.email, user.email)
        self.assertEqual(self.username, user.username)
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertFalse(user.is_deleted)
    
    def test_user_name_required(self):
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(email = self.email, username = '')
    
    def test_email_required(self):
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(email = '', username = self.username)
