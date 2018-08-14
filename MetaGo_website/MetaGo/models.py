from django.db import models
from django.contrib.postgres import fields as postgres_fields

# Create your models here.
class Employee(models.Model):
    person_id = models.CharField(max_length=10, null=True, blank=True)
    face_encoding = postgres_fields.ArrayField(models.FloatField(null=True, blank=True), size=128, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    debt = models.FloatField(null=True, blank=True)

class Snack(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
