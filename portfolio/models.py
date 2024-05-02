from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)  
    category = models.CharField(max_length=100)  
    image_description = models.TextField(blank=True) 
    image = models.ImageField(upload_to='images/') 