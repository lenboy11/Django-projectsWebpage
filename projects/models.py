from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from math import ceil, floor
from django.urls import reverse
from cloudinary.models import CloudinaryField
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(default='A brief description' , max_length=100)
    category = models.CharField(default='coding', max_length=30)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # frontpic = models.ImageField(default='front_pics/default_post.png', upload_to='front_pics')
    frontpic = CloudinaryField('image')
    url = models.CharField(default="#", max_length=50)
    active = models.BooleanField(default=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

    # def save(self):
    #     super().save()
    #     img = Image.open(self.frontpic.path)
    #     if img.format != "GIF":
    #         w = img.width
    #         h = img.height
    #         rel = h/w
    #         h0 = h
    #         padh = 0
    #         w0 = w
    #         padw = 0
    # 
    #         if rel > 3/2:
    #             h0 = ceil(w*3/2)
    #             padh = floor((h - h0)/2)
    #         elif rel < 3/2:
    #             w0 = ceil(h*2/3)
    #             padw = floor((w - w0)/2)
    #         size = (min(w0,800), min(h0,1200))
    #         box = (padw, padh, w0+padw, h0+padh)
    #
    #         img = img.resize(size, box=box)
    #         img.save(self.frontpic.path)



class Link(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(default='https://www.google.de/' , max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    platform = models.CharField(default='coding', max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + ": " + self.url

    def get_absolute_url(self):
        return reverse('link-detail', kwargs={'pk': self.pk})