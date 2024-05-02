from django.db import models

class Service(models.Model):
    icon_choices = [
        ('bi-briefcase', 'Briefcase'),
        ('bi-card-checklist', 'Card Checklist'),
        ('bi-bar-chart', 'Bar Chart'),
        ('bi-binoculars', 'Binoculars'),
        ('bi-brightness-high', 'Brightness High'),
        ('bi-calendar4-week', 'Calendar Week'),
    ]
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, choices=icon_choices, default='bi-briefcase')
    description = models.TextField()
