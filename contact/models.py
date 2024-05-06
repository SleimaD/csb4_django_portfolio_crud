from django.db import models

class ContactInfo(models.Model):
    description = models.TextField()
    street = models.CharField(max_length=200)
    street_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
