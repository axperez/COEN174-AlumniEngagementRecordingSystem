'''Alumni Engagement Recording System | Developers: Axel Perez, Brendan Watamura, & Matt Wong -->
models.py
This file contains the models that define the databases entities. Each model contains attributes that link the database and python classes together.
The Alumni model contains the attributes collected on hosts and attendees. The Events model contains attributes pertaining to event details, which
is pertinent to a full reporting system.
'''

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Alumni(models.Model):
	Name = models.CharField(max_length=40, primary_key=True)
	DOB = models.DateField()
	Email = models.EmailField(unique=True)
	Grad_Year = models.CharField(max_length=4)
	Job_Title = models.CharField(max_length=30, null=True)
	Phone_Num = models.CharField(max_length=15, null=True)
	STATUSES = (
        (u'Pending', u'Pending'),
        (u'Accepted', u'Accepted'),
        (u'Denied', u'Denied'),
    )
	Verified = models.CharField(max_length=8, choices=STATUSES, default = 'Pending')

	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse('site-home')

	class Meta:
		verbose_name_plural = 'alumni'

class Events(models.Model):
	EID = models.AutoField(primary_key=True)
	Title = models.CharField(max_length=20)
	Description = models.TextField()
	Edate = models.DateField()
	Start_Time = models.TimeField()
	End_Time = models.TimeField()
	Address = models.CharField(max_length=30)
	City = models.CharField(max_length=15)
	State = models.CharField(max_length=15)
	Zipcode = models.CharField(max_length=5)
	Country = models.CharField(max_length=20)
	ConfCode = models.CharField(max_length=20)
	STATUSES = (
        (u'Pending', u'Pending'),
        (u'Accepted', u'Accepted'),
        (u'Denied', u'Denied'),
        (u'Past', u'Past'),
    )
	Request_Status = models.CharField(max_length=8, choices=STATUSES, default = 'Pending')
	Eattendants = models.ManyToManyField(Alumni, related_name='attendants_list', blank=True)
	Ersvp = models.ManyToManyField(Alumni, related_name='rsvp_list', blank=True)
	Ehosts = models.ManyToManyField(Alumni, related_name='userhosts', blank = True)

	def __str__(self):
		return self.Title

	def get_absolute_url(self):
		return reverse('site-home')

	class Meta:
		verbose_name_plural = 'events'
