from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Alumni, Events

class AlumniForm(forms.Form):
    #AID = forms.AutoField(primary_key=True)
    #UserID = forms.ForeignKey(Users, on_delete=forms.CASCADE, related_name = 'are_alumni')
    Fname = forms.CharField(max_length=15)
    Minit = forms.CharField(max_length=1, required=False)
    Lname = forms.CharField(max_length=15)
    DOB = forms.DateField()
    Email = forms.EmailField()
    Grad_Year = forms.CharField(max_length=4)
    Job_Title = forms.CharField(max_length=30)
    Phone_Num = forms.CharField(max_length=15)
    Address = forms.CharField(max_length=30)
    City = forms.CharField(max_length=15)
    State = forms.CharField(max_length=15)
    Zipcode = forms.CharField(max_length=5)
    Country = forms.CharField(max_length=20)
    EventAttending = forms.ModelMultipleChoiceField(Events.objects.all())
