from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default = "profile_pics/default_profile.png", upload_to = "profile_pics")
    image = CloudinaryField('image')
    bio = models.TextField()
    linkedIn = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    spotify = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     h = img.height
    #     w = img.width
    #     rel = h/w
    #     if rel == 1:
    #         size = (min(300,w), min(300,h))
    #         box = (0,0, w, h)
    #     elif rel > 1:
    #         pad = (h-w)/2
    #         size = (min(300, w), min(300,w))
    #         box = (0, pad, w, h-pad)
    #     else:
    #         pad = (w - h)/2
    #         size = (min(300, h), min(300,h))
    #         box = (pad, 0, w-pad, h)
    #
    #     img = img.resize(size, box=box)
    #     img.save(self.image.path)