# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField(default=timezone.now)
	location = models.CharField(max_length=100)
	content = models.TextField()
	firstname = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
