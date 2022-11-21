"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTEsts(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test if the email is being normalized for a new user"""
        sample_emails = [
            ['test1@example.com', 'test1@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_with_no_email_fails(self):
        """Test if a new user with no email raises an exception"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user('', 'sample123') # noqa

    def test_create_new_superuser(self):
        """Test creating a superuser"""
        superuser = get_user_model().objects.create_superuser(
            'test_super@example.com',
            'admin123'
        )

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
