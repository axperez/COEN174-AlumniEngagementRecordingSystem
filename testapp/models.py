# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
'''
class Event(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField(default=timezone.now)
	location = models.CharField(max_length=100)
	content = models.TextField()
	firstname = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('event-view', kwargs={'pk': self.pk})
'''

class Users(models.Model):
	UID = models.AutoField(primary_key=True)
	User_Type = ('Admin', 'Alumni')

	def __str__(self):
		return 'UserID: ' + self.UID

	def get_absolute_url(self):
		return reverse('event-view', kwargs={'pk': self.UID})

class Alumni(models.Model):
	AID = models.AutoField(primary_key=True)
	UserID = models.ForeignKey(Users, on_delete=models.CASCADE, related_name = 'are_alumni')
	Fname = models.CharField(max_length=15)
	Minit = models.CharField(max_length=1, blank = True)
	Lname = models.CharField(max_length=15)
	DOB = models.DateField()
	Email = models.EmailField()
	Grad_Year = models.CharField(max_length=4)
	Job_Title = models.CharField(max_length=30)
	Phone_Num = models.CharField(max_length=15)
	Address = models.CharField(max_length=30)
	City = models.CharField(max_length=15)
	State = models.CharField(max_length=15)
	Zipcode = models.CharField(max_length=5)
	Country = models.CharField(max_length=20)
	#is_user = models.OneToOneField(Users, on_delete=models.CASCADE)

	def __str__(self):
		return self.Fname + ' ' + self.Minit + ' ' + self.Lname

	def get_absolute_url(self):
		return reverse('event-view', kwargs={'pk': self.AID})

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
	Request_Status = ('Pending', 'Accepted', 'Denied')
	Eattendants = models.ManyToManyField(Users, through = 'Attends', related_name='attendants')
	Ehosts = models.ManyToManyField(Users, through = 'Hosts', related_name='userhosts')

	def __str__(self):
		return self.Title

	def get_absolute_url(self):
		return reverse('event-view', kwargs={'pk': self.EID})

class Attends(models.Model):
	UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
	EventID = models.ForeignKey(Events, on_delete=models.CASCADE)


class Hosts(models.Model):
	UsID = models.ForeignKey(Users, on_delete=models.CASCADE)
	EvID = models.ForeignKey(Events, on_delete=models.CASCADE)
