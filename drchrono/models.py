from django.db import models

from datetime import date

# Create your models here.


class Patient(models.Model):
    pass;
    # first_name = models.CharField(max_length=20);
    # last_name = models.CharField(max_length=20);
    # doctor = models.PositiveIntegerField(max_length=12);
    # gender = models.CharField(max_length=60);
    # #date_of_birth = models.DateField(default=date.now());
    # chart_id = models.IntegerField(max_length=12);
    # id = models.IntegerField(max_length=12);


# python manage.py makemigrations
# python manage.py migrate