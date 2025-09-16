from django.db import models

# Create your models here.
# events/models.py
from django.db import models

# Django automatically creates an id as auto-increment PK if not specified

class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    zip_code = models.CharField(max_length=10)
    capacity = models.IntegerField()
    notes = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    contact = models.CharField(max_length=20)
    notes = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    expense = models.DecimalField(max_digits=9, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    artists = models.ManyToManyField('Artist', blank=True)
    notes = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.start_date}"