from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Thing(models.Model):
    name = models.CharField(
        blank=False,
        max_length=30,
        unique=True
    )
    description = models.CharField(
        max_length=120,
        blank=True,
        unique=False
    )
    quantity = models.IntegerField(
        unique=False,
        validators=[
            MaxValueValidator(limit_value = 100, message = "value above 100"),
            MinValueValidator(limit_value = 0, message = "value below 0")
            ]
        )
