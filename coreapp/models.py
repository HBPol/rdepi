from django.db import models

# Extending AbstractUser to create a custom user model
from django.contrib.auth.models import AbstractUser
class User (AbstractUser):
    date_left = models.CharField(max_length=30)
    projects = models.CharField(max_length=30)
    author_of = models.CharField(max_length=30)
    def __str__(self):
        return self.get_fullname()

