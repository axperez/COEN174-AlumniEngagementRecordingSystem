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
from .models import Event

# Create your views here.

def home(request):
	context = {
		'events': Event.objects.all()
	}
	return render(request, 'testapp/home.html', context)

class PostListView(ListView):
	model = Event
	template_name = 'testapp/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'events'
	ordering = ['-date']

def about(request):
	return render(request, 'testapp/about.html', {'title': 'About'})

class PostDetailView(DetailView):
	model = Event
	
class PostCreateView(CreateView):
	model = Event
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.firstname = self.request.user
		return super().form_valid(form)

class PostUpdateView(UpdateView):
	model = Event
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.firstname = self.request.user
		return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Event
	success_url ='/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == event.firstname:
			return True
		return False

