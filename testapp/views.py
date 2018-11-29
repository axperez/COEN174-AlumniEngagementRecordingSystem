'''
Alumni Engagement Recording System | Developers: Axel Perez, Brendan Watamura, & Matt Wong

views.py

This file handles how a python function can take a web request and return a web response. We specify which model a certain view will need to use,
any context or form information that we would like to add, and any displays that we want to render or return.
'''

from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView
)

from django.http import HttpResponse, HttpResponseRedirect
from .models import Alumni, Events
from .forms import AlumniForm, RsvpForm, CreatEventForm, ConfCodeForm
from .helper import unique_conf_code, sendmail


def home(request):
	'''
	View function to show all of the events on the home page.
	'''
	context = {
		'events': Events.objects.all()
	}
	return render(request, 'testapp/home.html', context)

def event_detail(request, pk):
	'''
	View function to display event report and buttons to accept, deny, edit, confirmation code, and archive.
	'''
	event = Events.objects.get(EID=pk)

	#Only if buttons are pressed
	if request.method == 'POST':
		status = request.POST.get('status')
		event.Request_Status = status
		event.save()
		eventname = pk
		if status == 'Accepted':
			if ' ' in pk:
				eventname = pk.replace(' ', '%20')
			sendmail(event.Title, (event.Ehosts.all())[0].Email, status, event.ConfCode, 'http://axperez.pythonanywhere.com/event/%s/checkin'%eventname)
		elif status == 'Denied':
			sendmail(event.Title, (event.Ehosts.all())[0].Email, status)

	args = {'object':event}

	return render(request, 'testapp/events_detail.html', args)


class PostListView(ListView):
	'''
	View class to list events on home page in the order of soonest date.
	'''
	model = Events
	template_name = 'testapp/home.html'
	context_object_name = 'events'
	ordering = ['-Edate']

class AlumniListView(ListView):
	'''
	View class to list the alumni.
	'''
	model = Alumni
	context_object_name = 'alumni'

class EventCreateView(FormView):
	'''
	View class to use a form to create new events. Both event and alumni objects are populated.
	'''
	template_name = 'testapp/events_form.html'
	form_class = CreatEventForm

	def form_valid(self, form):
		Name = form.cleaned_data['Host_Name']
		DOB = form.cleaned_data['Host_DOB']
		Email = form.cleaned_data['Host_Email']
		Grad_Year = form.cleaned_data['Host_Grad_Year']
		Job_Title = form.cleaned_data['Host_Job_Title']
		Phone_Num = form.cleaned_data['Host_Phone_Number']
		Title = form.cleaned_data['Title']
		Description = form.cleaned_data['Description']
		Edate = form.cleaned_data['Edate']
		Start_Time = form.cleaned_data['Start_Time']
		End_Time = form.cleaned_data['End_Time']
		Address = form.cleaned_data['Address']
		City = form.cleaned_data['City']
		State = form.cleaned_data['State']
		Zipcode = form.cleaned_data['Zipcode']
		Country = form.cleaned_data['Country']

		#Create alumni object
		alumni = Alumni(Name = Name, DOB = DOB, Email = Email, Grad_Year = Grad_Year, Job_Title = Job_Title, Phone_Num = Phone_Num)
		alumni.save()

		#Generate confirmation code through helper.py function
		confcode = unique_conf_code(Events.objects.all())

		#Create event object
		event = Events(Title = Title, Description = Description, Edate = Edate, Start_Time = Start_Time, End_Time = End_Time, Address = Address, City = City, State = State, Zipcode = Zipcode, Country = Country, ConfCode = confcode)
		event.save()
		#Connect alumni created to the event created as a host
		event.Ehosts.add(alumni)
		event.save()

		#return home
		return HttpResponseRedirect('/')

class PostUpdateView(UpdateView):
	'''
	View class to edit an event.
	'''
	model = Events
	fields = ['Title', 'Description', 'Edate', 'Start_Time', 'End_Time', 'Address', 'City', 'State', 'Zipcode', 'Country']

	def form_valid(self, form):
		form.instance.firstname = self.request.user
		return super().form_valid(form)

def verify_alumni(request):
	'''
	Show alumni that have not been verified yet and provide buttons to accept/deny alumni verification.
	'''
	#If any button pressed
	if request.method == 'POST':
		pk = request.POST.get('alumname')
		alum = Alumni.objects.get(Name=pk)
		status = request.POST.get('status')
		#Set status to accept/deny
		alum.Verified = status
		alum.save()

	args = {'alumni':Alumni.objects.all()}

	return render(request, 'admin/alumnipending.html', args)


class CheckinCreateView(FormView):
	'''
	View class to check in using a form that populates alumni and the event's attending list.
	'''
	template_name = 'testapp/checkin.html'
	form_class = AlumniForm

	def form_valid(self, form):
		Name = form.cleaned_data['Name']
		DOB = form.cleaned_data['DOB']
		Email = form.cleaned_data['Email']
		Grad_Year = form.cleaned_data['Grad_Year']
		Job_Title = form.cleaned_data['Job_Title']
		Phone_Num = form.cleaned_data['Phone_Num']
		EventAttending = form.cleaned_data['EventAttending']

		#Create alumni object
		alumni = Alumni(Name = Name, DOB = DOB, Email = Email, Grad_Year = Grad_Year, Job_Title = Job_Title, Phone_Num = Phone_Num)
		alumni.save()

		#Find event object
		event = Events.objects.get(EID=EventAttending[0].EID)
		#Add alumni to event attendance list
		event.Eattendants.add(alumni)
		event.save()

		#return to event detail page
		return HttpResponseRedirect('/event/%s' % EventAttending[0].EID)

class RsvpCreateView(FormView):
	'''
	View class to rsvp using a form that populates alumni and the event's rsvp list.
	'''
	template_name = 'testapp/rsvp.html'
	form_class = RsvpForm

	def form_valid(self, form):
		Name = form.cleaned_data['Name']
		DOB = form.cleaned_data['DOB']
		Email = form.cleaned_data['Email']
		Grad_Year = form.cleaned_data['Grad_Year']
		Job_Title = form.cleaned_data['Job_Title']
		Phone_Num = form.cleaned_data['Phone_Num']
		EventAttending = form.cleaned_data['EventAttending']

		#Create alumni object
		alumni = Alumni(Name = Name, DOB = DOB, Email = Email, Grad_Year = Grad_Year, Job_Title = Job_Title, Phone_Num = Phone_Num)
		alumni.save()

		#Find event object
		event = Events.objects.get(EID=EventAttending[0].EID)

		#Add alumni to event attendance list
		event.Ersvp.add(alumni)
		event.save()

		#return to event detail page
		return HttpResponseRedirect('/event/%s' % EventAttending[0].EID)

class ConfCodeView(FormView):
	'''
	View class to check if provided confirmation code matches the event's code.
	If yes, then send to update page.
	'''
	template_name = 'testapp/confcode.html'
	form_class = ConfCodeForm

	def form_valid(self, form):
		'''
		Function to retrieve confirmation code and check if it exists in our
		database. If there is an error, tell user that code is incorrect.
		'''
		confcode = form.cleaned_data['Confirmation_Code']
		try:
			 event = Events.objects.get(ConfCode=confcode)
			 flag = True
		except Exception as e:
			print (e)
			flag = False

		#If confirmation code matched an event, send to update page
		if flag:
			return HttpResponseRedirect('/event/%s/update' % event.EID)

		#Else, tell user to try again
		messages.error(self.request,'Confirmation Code Incorrect')
		return HttpResponseRedirect(self.request.path_info)
