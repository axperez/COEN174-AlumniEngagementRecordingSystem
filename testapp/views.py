# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView
)

from django.http import HttpResponse
from .models import Alumni, Events
from .forms import AlumniForm

# Create your views here.

def home(request):
	context = {
		'events': Events.objects.all()
	}
	return render(request, 'testapp/home.html', context)

class PostListView(ListView):
	model = Events
	template_name = 'testapp/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'events'
	ordering = ['-Edate']

def about(request):
	return render(request, 'testapp/about.html', {'title': 'About'})

class PostDetailView(DetailView):
	model = Events

class PostCreateView(CreateView):
	model = Events
	fields = ['Title', 'Description', 'Edate', 'Start_Time', 'End_Time', 'Address', 'City', 'State', 'Zipcode', 'Country']

	def form_valid(self, form):
		form.instance.firstname = self.request.user
		return super().form_valid(form)

class PostUpdateView(UpdateView):
	model = Events
	fields = ['Title', 'Description', 'Edate', 'Start_Time', 'End_Time', 'Address', 'City', 'State', 'Zipcode', 'Country']

	def form_valid(self, form):
		form.instance.firstname = self.request.user
		return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Events
	success_url ='/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == event.Fname:
			return True
		return False

class CheckinCreateView(FormView):
	#model = Alumni
	#fields = ['Fname', 'Minit', 'Lname', 'DOB', 'Email', 'Grad_Year', 'Job_Title', 'Phone_Num', 'Address', 'City', 'State', 'Zipcode', 'Country']
	template_name = 'testapp/checkin.html'
	form_class = AlumniForm

	def form_valid(self, form):
		Fname = form.cleaned_data['Fname']
		Minit = form.cleaned_data['Minit']
		Lname = form.cleaned_data['Lname']
		DOB = form.cleaned_data['DOB']
		Email = form.cleaned_data['Email']
		Grad_Year = form.cleaned_data['Grad_Year']
		Job_Title = form.cleaned_data['Job_Title']
		Phone_Num = form.cleaned_data['Phone_Num']
		Address = form.cleaned_data['Address']
		City = form.cleaned_data['City']
		State = form.cleaned_data['State']
		Zipcode = form.cleaned_data['Zipcode']
		Country = form.cleaned_data['Country']
		#EventAttending = form.cleaned_data['EventAttending']

		alumni = Alumni(Fname = Fname, Minit = Minit, Lname = Lname, DOB = DOB, Email = Email, Grad_Year = Grad_Year, Job_Title = Job_Title, Phone_Num = Phone_Num, Address = Address, City = City, State = State, Zipcode = Zipcode, Country = Country)
		alumni.save()

		#event = Events.objects.get(pk=EventAttending)
		#event.Eattendants.add(str(Fname))
		#attends = Attends(AlumFname=Fname, EventTitle=EventAttending)
		#attends.save()



class AlumniVerificationCreateView(CreateView):
	model = Alumni
	fields = ['Fname', 'Minit', 'Lname', 'DOB', 'Email', 'Grad_Year', 'Job_Title', 'Phone_Num', 'Address', 'City', 'State', 'Zipcode', 'Country']
