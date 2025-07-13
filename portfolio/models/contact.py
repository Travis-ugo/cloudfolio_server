from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, region='NG') 
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    calendly_link = models.URLField(blank=True)

    def __str__(self):
        return f"Public Contact Info"
