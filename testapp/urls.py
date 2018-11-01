from __future__ import unicode_literals
from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	CheckinCreateView,
	AlumniVerificationCreateView
)
from . import views

urlpatterns = [
		path('', PostListView.as_view() , name='site-home'),
		path('event/<str:pk>/', PostDetailView.as_view() , name='event-view'),
		path('create/new/', PostCreateView.as_view() , name='event-create'),
		path('event/<str:pk>/update/', PostUpdateView.as_view() , name='event-update'),
		path('event/<str:pk>/delete/', PostDeleteView.as_view() , name='event-delete'),
		path('event/<str:pk>/checkin/', CheckinCreateView.as_view(template_name="testapp/checkin.html/") , name='event-checkin'),
		path('alumniverification/', AlumniVerificationCreateView.as_view(template_name="testapp/alumniverification.html/") , name='alumni-verif'),
		path('about/', views.about, name='site-about'),
]
