from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    
    def test_creates_user(self):
        user = User.objects.create_user('admin','admin@gmail.com','admin123!@')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'admin@gmail.com')
        self.assertEqual(user.username, 'admin')
        
    def test_creates_super_user(self):
        user = User.objects.create_superuser('admin','admin@gmail.com','admin123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'admin@gmail.com')
        self.assertEqual(user.username, 'admin')
        
    def test_raises_error_if_username_not_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="",email="admin@gmail.com",password="admin123!@")
        
    def test_raises_error_if_email_not_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="admin",email="",password="admin123!@")
        
    def test_raises_error_if_superuser_created_without_is_staff_status(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='admin',email='admin@gmail.com',password='admin123!@',is_staff=False)
            
    def test_raises_error_if_superuser_created_without_superuser_status(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='admin',email='admin@gmail.com',password='admin123!@',is_superuser=False)