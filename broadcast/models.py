from django.db import models

# Create your models here.
class Broadcast(models.Model):
    name                = models.CharField(max_length=60)
    youtube_link        = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name