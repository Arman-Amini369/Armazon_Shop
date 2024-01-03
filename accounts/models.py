from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomerAccount(AbstractUser):
    username = PhoneNumberField(region="IR", unique=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'  
