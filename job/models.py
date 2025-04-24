from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from django.contrib.auth.models import User
import os
# Create your models here.



class JobType(models.TextChoices):
    Permanent = "Permanent"
    Temporaty = "Temporaty"
    InternShip = "InternShip"


class Education(models.TextChoices):
    Diploma = "Diploma"
    Bachelors = "Bachelors"
    Master = "Master"
    Phd = "Phd"


class Industry(models.TextChoices):
    Business = "Business"
    IT = "IT"
    DesignAndTextile = "DesignAndTextile"
    Banking = "Banking"
    Education = "Education"
    Telecommunication = "Telecommunication"
    Sales="Sales"
    Others = "Others"

class Experience(models.TextChoices):
    NO_EXPERIENCE = "NO_EXPERIENCE"
    ONE_YEAR = "ONE_YEAR"
    TWO_YEAR = "TWO_YEAR"
    THREE_YEAR= "THREE_YEAR"
    FOUR_YEAR_PLUS = "FOUR_YEAR_PLUS"



def return_date_time():
    return datetime.now() + timedelta(days=10)



class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    job_type = models.CharField(max_length=20, choices=JobType.choices, default=JobType.Permanent)
    education = models.CharField(max_length=20, choices=Education.choices, default=Education.Bachelors)
    industry = models.CharField(max_length=20, choices=Industry.choices, default=Industry.Business)
    experience = models.CharField(max_length=20, choices=Experience.choices, default=Experience.NO_EXPERIENCE)
    salary = models.IntegerField(default=1, null=True)
    positions = models.IntegerField(default=1, null=True)
    compnay = models.CharField(max_length=100, null=True)
    last_date = models.DateField(default=return_date_time)
    created_at = models.DateTimeField(auto_now_add=True)

