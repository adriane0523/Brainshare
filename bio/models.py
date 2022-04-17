from django.db import models

# Create your models here.

class Co_Principal_Investigators(models.Model):
    name = models.CharField(max_length=255)
    profession = models.TextField(default="")
    place = models.CharField(max_length=255, blank=True, default="")
    bio = models.TextField()
    image = models.CharField(max_length=50)

class Co_Investigators(models.Model):
    name = models.CharField(max_length=255)
    profession = models.TextField(default="")
    place = models.CharField(max_length=255, blank=True, default="")
    bio = models.TextField()
    image = models.CharField(max_length=50)

class Project_Personnel(models.Model):
    name = models.CharField(max_length=255)
    profession = models.TextField(default="")
    place = models.CharField(max_length=255, blank=True, default="")
    bio = models.TextField()
    image = models.CharField(max_length=50)
    view = models.BooleanField(default=True)

class Advisory_Comitee(models.Model):
    name = models.CharField(max_length=255)
    profession = models.TextField(default="")
    place = models.CharField(max_length=255, blank=True, default="")
    bio = models.TextField()
    image = models.CharField(max_length=50)
    
