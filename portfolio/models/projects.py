from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    images = models.JSONField(blank=True, null=True, default=list)
    videos = models.JSONField(blank=True, null=True, default=list)
    github_link = models.URLField(blank=True, null=True)
    playstore_link = models.URLField(blank=True, null=True)
    appstore_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title