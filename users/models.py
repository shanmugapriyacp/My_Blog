from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    post_title = models.CharField(max_length=200, null=False)
    post_content = models.TextField(default='post content')
    date_published = models.DateField(blank=True, null=True)
