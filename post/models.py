from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User)
	content = models.TextField(max_length=140)
	created_at = models.DateTimeField(auto_now=True)

	def __repr__(self):
		return "Post(%s, %s)" % (self.user.username, self.created_at)
