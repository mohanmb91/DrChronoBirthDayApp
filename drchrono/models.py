from django.db import models

from datetime import datetime as date

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=20);
    last_name = models.CharField(max_length=20);
    doctor = models.PositiveIntegerField();
    gender = models.CharField(max_length=60);
    date_of_birth = models.CharField(default=str(date.now()), max_length= 10);
    chart_id = models.IntegerField();
    id = models.IntegerField(max_length=12,primary_key=True);


# python manage.py makemigrations
# python manage.py migrate

class User(models.Model):
    user_name = models.CharField(max_length=20);
    access_token = models.CharField(max_length=100);