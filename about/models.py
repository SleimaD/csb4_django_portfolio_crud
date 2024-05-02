from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='images/')
    general_description = models.TextField()
    birthday = models.DateField()
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance = models.CharField(max_length=100)
    detailed_description = models.TextField()    