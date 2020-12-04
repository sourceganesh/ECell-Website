from django.db import models

# Create your models here.
class Startup(models.Model):
    startup_name = models.CharField(max_length=200)
    email = models.EmailField()
    team_size = models.IntegerField()
    stage = models.CharField(max_length=200)
    year_formed = models.IntegerField()
    industry = models.CharField(max_length=200)
    startup_description = models.TextField()
    pitch_link = models.URLField(blank=True)
    website_link=models.URLField(blank=True)
