'''Alumni Engagement Recording System | Developers: Axel Perez, Brendan Watamura, & Matt Wong -->
forms.py
This file contains the forms that we created for use throughout our website. Some forms we used Django templates to create
however these are our custom forms.
'''

from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import Alumni, Events

class AlumniForm(forms.Form):
    Name = forms.CharField(max_length=40)
    DOB = forms.DateField()
    Email = forms.EmailField()
    Grad_Year = forms.CharField(max_length=4)
    Job_Title = forms.CharField(max_length=30, required=False)
    Phone_Num = forms.CharField(max_length=15, required=False)
    EventAttending = forms.ModelMultipleChoiceField(Events.objects.all())

class RsvpForm(forms.Form):
    Name = forms.CharField(max_length=40)
    DOB = forms.DateField()
    Email = forms.EmailField()
    Grad_Year = forms.CharField(max_length=4)
    Job_Title = forms.CharField(max_length=30, required=False)
    Phone_Num = forms.CharField(max_length=15, required=False)
    EventAttending = forms.ModelMultipleChoiceField(Events.objects.all())

class CreatEventForm(forms.Form):
    Host_Name = forms.CharField(max_length=40)
    Host_DOB = forms.DateField()
    Host_Email = forms.EmailField()
    Host_Grad_Year = forms.CharField(max_length=4)
    Host_Phone_Number = forms.CharField(max_length=15)
    Host_Job_Title = forms.CharField(max_length=30, required=False)
    Title = forms.CharField(max_length=20)
    Description = forms.CharField(max_length=200)
    Edate = forms.DateField()
    Start_Time = forms.TimeField()
    End_Time = forms.TimeField()
    Address = forms.CharField(max_length=30)
    City = forms.CharField(max_length=15)
    State = forms.CharField(max_length=15)
    Zipcode = forms.CharField(max_length=5)
    Country = forms.CharField(max_length=20)

class ConfCodeForm(forms.Form):
    Confirmation_Code = forms.CharField(max_length=20)
