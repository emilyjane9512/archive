from django.conf import settings
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()

# Create your models here.
