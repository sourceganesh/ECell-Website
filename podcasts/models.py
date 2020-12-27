from django.db import models

# Create your models here.
class Podcast(models.Model):
    name                = models.CharField(max_length=60)
    description         = models.CharField(max_length=600)
    spotify_smug        = models.CharField(max_length=30)
    youtube_link        = models.CharField(max_length=150)
    image               = models.ImageField(upload_to = 'podcasts/')
    pass