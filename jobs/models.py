from datetime import date
from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from math import ceil, floor
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)

class Country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)

class Language(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return str(self.name)

class Company(models.Model):
    name = models.CharField(max_length=60)
    homepage = models.URLField(null=True)
    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        if self.homepage == None:
            self.homepage = "https://www.google.com/search?q=" + str(self.name)
        super().save(*args, **kwargs)

class Job(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default='A brief description')
    skills = models.ManyToManyField(Skill, null=True)
    country = models.ForeignKey(Country, null=True, on_delete=SET_NULL)
    city = models.ForeignKey(City, null=True, on_delete=SET_NULL)
    language = models.ForeignKey(Language, null=True, on_delete=SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=SET_NULL)
    date_posted = models.DateField(default=date.today)
    url = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str( str(self.title) + " | in " + str(self.country) + " (" + str(self.city) + ")")

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # check if city and country match
        if (not self.city == None) and (not self.country == self.city.country):
            c = self.city.country
            for city in City.objects.all().filter( name = self.city.name ):
                if self.country == city.country:
                    self.city = city
                    c = city.country
                    break
        self.country = c
        super().save(*args, **kwargs)

