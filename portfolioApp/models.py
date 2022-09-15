from email.headerregistry import Address
from django.db import models

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = "master"

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
)

class UserProfile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=25, default='')
    Mobile = models.CharField(max_length=10, default='')
    BirthDate = models.DateField()
    Gender = models.CharField(max_length=5, choices=gender_choices)
    Country = models.CharField(max_length=15, default='')
    State = models.CharField(max_length=15, default='')
    City = models.CharField(max_length=15, default='')
    Address = models.TextField(max_length=200, default='')
    
    class Meta:
        db_table = 'userprofile'