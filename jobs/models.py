from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from math import ceil, floor
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=3)
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

class Company(models.Model):
    name = models.CharField(max_length=60)
    homepage = models.URLField()
    def __str__(self):
        return str(self.name)

class Job(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default='A brief description')
    skills = models.ManyToManyField(Skill, null=True)
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    category = models.CharField(default='coding', max_length=30)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    url = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str( str(self.title) + " | in " + str(self.country) + " (" + str(self.city) + ")")

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
