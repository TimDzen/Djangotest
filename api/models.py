from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('supplier', 'Поставщик'),
        ('consumer', 'Потребитель'),
    )
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

class Warehouse(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=20)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(Default = 0)
