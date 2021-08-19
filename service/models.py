from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth import get_user_model


class DriverUser(AbstractUser):
	name = models.CharField(max_length=250, default='Name')
	def __str__(self):
		return self.username

