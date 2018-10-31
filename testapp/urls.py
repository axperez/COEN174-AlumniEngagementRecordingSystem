from __future__ import unicode_literals
from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	CheckinCreateView
)
from . import views

urlpatterns = [
		path('', PostListView.as_view() , name='site-home'),
		path('event/<int:pk>/', PostDetailView.as_view() , name='event-view'),
		path('event/new/', PostCreateView.as_view() , name='event-create'),
		path('event/<int:pk>/update/', PostUpdateView.as_view() , name='event-update'),
		path('event/<int:pk>/delete/', PostDeleteView.as_view() , name='event-delete'),
		path('event/<int:pk>/checkin/', CheckinCreateView.as_view(template_name="testapp/checkin.html/") , name='event-checkin'),
		path('about/', views.about, name='site-about'),
]
