import random
import string

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models, IntegrityError


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have valid Email')
        if extra_fields:
            pass

        """creates and saves a new user"""
        user = self.model(email=email.lower(), **extra_fields)
        user.set_password(password)
        # ensures user.uid is unique
        try:
            user.save(using=self._db)
        except IntegrityError:
            extra_fields['uid'] = create_unique_id()
            self.create_user(self, email, password, **extra_fields)

        return user

    def create_superuser(self, email, password):
        # TODO: validation for duplicate uid value
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


def create_unique_id():
    # sample random hex id generator
    return 'W' + ''.join(random.choices(string.hexdigits, k=8)).upper()


class User(AbstractBaseUser, PermissionsMixin):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    uid = models.CharField(max_length=9, default=create_unique_id, unique=True)
    real_name = models.CharField(max_length=255)
    tz = models.CharField(max_length=32, choices=TIMEZONES,
                          default='UTC')

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'({self.user}): {self.start_time},{self.end_time}'
