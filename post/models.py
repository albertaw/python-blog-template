from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	username = models.CharField(max_length=20)
	content = models.TextField(max_length=140)
	created_at = models.DateTimeField(auto_now=True)
