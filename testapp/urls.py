'''
Alumni Engagement Recording System | Developers: Axel Perez, Brendan Watamura, & Matt Wong

urls.py

This file handles our url paths.
'''

from __future__ import unicode_literals
from django.urls import path
from .views import (
	PostListView,
	AlumniListView,
	EventCreateView,
	PostUpdateView,
	CheckinCreateView,
	RsvpCreateView,
	ConfCodeView
)
from . import views
from django.conf.urls import include, url

urlpatterns = [
		path('', PostListView.as_view() , name='site-home'),
		path('admin/pending', PostListView.as_view(template_name="admin/pending.html/") , name='event-pending'),
		path('admin/past', PostListView.as_view(template_name="admin/past.html/") , name='event-past'),
		path('admin/alumni', AlumniListView.as_view(template_name="admin/alumni.html/") , name='alumni-list'),
		path('admin/alumnipending/', views.verify_alumni),
		path('event/<str:pk>/',views.event_detail),
		path('create/new/', EventCreateView.as_view(template_name='testapp/events_form.html') , name='event-create'),
		path('event/<str:pk>/update/', PostUpdateView.as_view() , name='event-update'),
		path('event/<str:pk>/rsvp/', RsvpCreateView.as_view(template_name="testapp/rsvp.html/") , name='event-rsvp'),
		path('event/<str:pk>/confcode/', ConfCodeView.as_view(template_name="testapp/confcode.html/") , name='conf-code'),
		path('event/<str:pk>/checkin/', CheckinCreateView.as_view(template_name="testapp/checkin.html/") , name='event-checkin')
]
