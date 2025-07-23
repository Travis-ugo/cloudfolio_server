from django.db import models
from ..utils import unique_slug_generator

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self).lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
