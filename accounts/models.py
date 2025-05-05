from datetime import timedelta
import random

from django.utils import timezone

from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class RoleChoices(models.TextChoices):
    LIBRARIAN = ('librarian', "Librarian")
    READER = ('reader', "Reader")
    ADMIN = ('admin', 'Admin')


class User(AbstractUser):
    phone_number = models.CharField(max_length=200)
    role = models.CharField(max_length=100, choices=RoleChoices.choices, default=RoleChoices.READER)
    balance = models.PositiveIntegerField(default=200)
    email = models.EmailField()


# class FileUpload(models.Model):


#     file = models.FileField(upload_to='file/')
#     name = models.CharField(max_length=255)

class UploadFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()

    class Meta:
        db_table = 'files'


def exp_time_now():
    return timezone.now() + timedelta(minutes=2)


def generate_code():
    return random.randint(100000, 999999)


class Code(models.Model):
    code = models.PositiveIntegerField(default=generate_code)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='code')
    expired_date = models.DateTimeField(default=exp_time_now)
