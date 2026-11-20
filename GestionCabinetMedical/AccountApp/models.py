from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class User(AbstractUser):
    pass


number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="le numéro doit contenir exactement 8 chiffres")


def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError("la date de naissance doit être antérieure à la date du jour")


class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)])
    phone = models.CharField(max_length=8, validators=[number_validator])
    specialties = models.ManyToManyField('Specialty', related_name='doctors')

    def __str__(self):
        return f"Dr {self.first_name} {self.last_name}"


class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_validator])
    phone = models.CharField(max_length=8, validators=[number_validator])
    birth_date = models.DateField(validators=[validate_past_date])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
