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
	context = {
		'events': Events.objects.all()
	}
	return render(request, 'testapp/home.html', context)

def event_detail(request, pk):
	event = Events.objects.get(EID=pk)

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
	model = Events
	template_name = 'testapp/home.html'
	context_object_name = 'events'
	ordering = ['-Edate']

class AlumniListView(ListView):
	model = Alumni
	context_object_name = 'alumni'

class EventCreateView(FormView):
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

		alumni = Alumni(Name = Name, DOB = DOB, Email = Email, Grad_Year = Grad_Year, Job_Title = Job_Title, Phone_Num = Phone_Num)
		alumni.save()

		confcode = unique_conf_code(Events.objects.all())

		event = Events(Title = Title, Description = Description, Edate = Edate, Start_Time = Start_Time, End_Time = End_Time, Address = Address, City = City, State = State, Zipcode = Zipcode, Country = Country, ConfCode = confcode)
		event.save()
		event.Ehosts.add(alumni)
		event.save()

		return HttpResponseRedirect('/')

class PostUpdateView(UpdateView):
	model = Events
	fields = ['Title', 'Description', 'Edate', 'Start_Time', 'End_Time', 'Address', 'City', 'State', 'Zipcode', 'Country']

	def form_valid(self, form):
		form.instance.firstname = self.request.user
		return super().form_valid(form)

def verify_alumni(request):

	if request.method == 'POST':
		pk = request.POST.get('alumname')
		alum = Alumni.objects.get(Name=pk)
		status = request.POST.get('status')
		alum.Verified = status
		alum.save()

	args = {'alumni':Alumni.objects.all()}

	return render(request, 'admin/alumnipending.html', args)


class CheckinCreateView(FormView):
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

		alumni = Alumni(Name = Name, DOB = DOB, Email = Email, Grad_Year = Grad_Year, Job_Title = Job_Title, Phone_Num = Phone_Num)
		alumni.save()

		event = Events.objects.get(EID=EventAttending[0].EID)
		event.Eattendants.add(alumni)
		event.save()

		return HttpResponseRedirect('/event/%s' % EventAttending[0].EID)

class RsvpCreateView(FormView):
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

		alumni = Alumni(Name = Name, DOB = DOB, Email = Email, Grad_Year = Grad_Year, Job_Title = Job_Title, Phone_Num = Phone_Num)
		alumni.save()

		event = Events.objects.get(EID=EventAttending[0].EID)

		event.Ersvp.add(alumni)
		event.save()

		return HttpResponseRedirect('/event/%s' % EventAttending[0].EID)

class ConfCodeView(FormView):
	template_name = 'testapp/confcode.html'
	form_class = ConfCodeForm

	def form_valid(self, form):
		confcode = form.cleaned_data['Confirmation_Code']
		try:
			 event = Events.objects.get(ConfCode=confcode)
			 flag = True
		except Exception as e:
			print (e)
			flag = False

		if flag:
			return HttpResponseRedirect('/event/%s/update' % event.EID)

		messages.error(self.request,'Confirmation Code Incorrect')
		return HttpResponseRedirect(self.request.path_info)
