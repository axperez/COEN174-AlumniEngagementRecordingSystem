# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

from django.http import HttpResponse
from .models import Users, Alumni, Events, Attends, Hosts

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

class CheckinCreateView(CreateView):
	model = Alumni
	fields = ['Fname', 'Minit', 'Lname', 'DOB', 'Email', 'Grad_Year', 'Job_Title', 'Phone_Num', 'Address', 'City', 'State', 'Zipcode', 'Country']

	def form_valid(self, form):
		form.instance.firstname = self.request.user
		return super().form_valid(form)
