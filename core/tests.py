# Create your tests here.
import pytz
from django.contrib.auth import get_user_model
from django.test import TestCase

from core.models import ActivityPeriod

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


def SampleUser(**kwargs):
    user = {
        'email': 'ansuman13@gmail.com',
        'password': 'test@123',
        'tz': TIMEZONES[0],
        'real_name': 'Harry Potter'
    }
    user.update(kwargs)
    user = get_user_model().objects.create_user(**user)
    return user


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        email = "Ansuman@yopmail.com"
        password = "kathmandu@123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            real_name='Sirus Black',
            tz=TIMEZONES[1]
        )
        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """checks if the user email is normalized"""
        email = "ansuman@YOPMAIL.com"
        user = get_user_model().objects.create_user(
            email=email,
            password="ansuman123",
            real_name='Serpius Snape'
        )
        self.assertEqual(email.lower(), user.email)

    def test_new_user_valid_email(self):
        """Tests if the new user email is not None"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test@123")

    def test_new_superuser_creation(self):
        """Tests the new superuser created for is_staff and is_superuser
        permissions"""

        user = get_user_model().objects.create_superuser(
            email="ansuman@yopmail.com",
            password='test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_different_uid_each_user(self):
        """ Test uid is different for two different users"""
        user1 = SampleUser()
        user2 = SampleUser(email='user2@yopmail.com',
                           password='kathmandu@123')
        self.assertNotEqual(user1.uid, user2.uid)

    def test_activity_model_insert_successful(self):
        """ Test activity model for insertion"""
        user = SampleUser()
        activity_instance = ActivityPeriod.object.create(
            user=user,
            start_time='Mar 1 2020  11:11AM',
            end_time='Mar 1 2020  2:00PM'
        )
        self.assertEqual(activity_instance.user, user)
