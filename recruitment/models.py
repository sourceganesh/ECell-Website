from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 255)
    roll_number = models.CharField(max_length = 8)
    phone = models.CharField(max_length=10)
    
    class meta:
        abstract = True
        

class ManagementTeamRecs(ContactInfo):
    answer1 = models.TextField(max_length= 3000)
    answer2 = models.TextField(max_length= 3000)
    answer3 = models.TextField(max_length= 3000)
    content_writing = models.BooleanField(default=False)
    media = models.BooleanField(default=False)
    web = models.BooleanField( default=False)

    def __str__(self):
        return self.name + ' - ' +self.roll_number 

class MediaTeamRecs(ContactInfo):
    area_of_interest = models.CharField(max_length = 200)
    skills = models.CharField(max_length = 200)
    answer1 = models.TextField(max_length= 3000)
    answer2 = models.TextField(max_length= 3000)
    answer3 = models.TextField(max_length= 3000)
    other_interests = models.CharField(max_length =200, default = "-")
    other_skills = models.CharField(max_length =200, default = "-")

    def __str__(self):
        return self.name + ' - ' +self.roll_number 

class WebTeamRecs(ContactInfo):
    interest = (("Frontend",1),("Backend",2),("Both",0))
    area_of_interest = models.IntegerField(choices = interest)
    skills = models.TextField(max_length= 3000)
    answer1 = models.TextField(max_length= 3000)
    answer2 = models.TextField(max_length= 3000)
    answer3 = models.TextField(max_length= 3000)
    other_skills = models.CharField(max_length =200, default = "-")

    def __str__(self):
        return self.name + ' - ' +self.roll_number  