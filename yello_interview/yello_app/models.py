from django.db import models

# Create your models here.

class ShortenedUrl(models.Model):
    full_url   = models.URLField(unique=True)
    short_code = models.CharField(max_length=6, unique=True)