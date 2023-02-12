from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

    """add this in setting.py
    AUTH_USER_MODEL = 'core.User'
    """

    # ab problem hai isko solv karne ke liye database delete karna hoga phle
