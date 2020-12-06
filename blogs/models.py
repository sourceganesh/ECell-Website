from django.db import models

# Create your models here.
class BlogPosts(models.Model):

    name = models.CharField(max_length=40)
    url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    