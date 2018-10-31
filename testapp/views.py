# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.

def home(request):
	context = {
		'events': Event.objects.all()
	}
	return render(request, 'testapp/home.html', context)

def about(request):
	return render(request, 'testapp/about.html', {'title': 'About'})
