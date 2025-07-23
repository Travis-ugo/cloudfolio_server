from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    location = models.CharField(max_length=100, blank=True)        
    profile_image = models.URLField(blank=True)           
    cv_link = models.URLField(blank=True, null=True)    

    def __str__(self):
        return self.name
