# accounts/models.py
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
import random

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    otp = models.CharField(max_length=6, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def generate_otp(self):
        self.otp = '{:06}'.format(random.randint(0, 999999))
        self.save()
