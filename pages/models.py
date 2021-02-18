from django.db import models

# Create your models here.

class Team(models.Model):
    def __str__(self):
        return self.first_name

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'pictures/')
    twitter_link = models.URLField(max_length=200)
