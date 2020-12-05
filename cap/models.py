from django.db import models

# Create your models here.
class CampusAmbassador(models.Model):
    
    name = models.CharField(max_length=30)
    roll_number = models.CharField(max_length=20)
    points = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    college = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    year_of_study = models.CharField(max_length=30)
    best_suited = models.CharField(max_length=400)
    key_strengths = models.CharField(max_length=400)
    anticipate_learning = models.CharField(max_length=400)
    past_experience = models.CharField(max_length=400)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.roll_number = self.roll_number.upper()
        self.email = self.email.lower()
        return super(CampusAmbassador, self).save(*args, **kwargs)