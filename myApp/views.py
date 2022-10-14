from django.forms import formset_factory
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView

from .models import GeeksModel
from .forms import GeeksForm
from .models import GeeksWithFieldModel


def index(request):
    return HttpResponse("Hello Geeks")


def home_view(request):
	context ={}

	# create object of form
	form = GeeksForm(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	context['form']= form
	return render(request, "home.html", context)


"""
def formset_view(request):
	context ={}

	# creating a formset
	GeeksFormSet = formset_factory(GeeksForm)
	formset = GeeksFormSet()
	
	# Add the formset to context dictionary
	context['formset']= formset
	return render(request, "home.html", context)
"""

def formset_view(request):
	context ={}

	# creating a formset and 5 instances of GeeksForm
	GeeksFormSet = formset_factory(GeeksForm, extra = 3)
	formset = GeeksFormSet(request.POST or None)
	
	# print formset data if it is valid
	if formset.is_valid():
		for form in formset:
			print(form.cleaned_data)
			
	# Add the formset to context dictionary
	context['formset']= formset
	return render(request, "home.html", context)


# importing formset_factory
from django.forms import modelformset_factory

def modelformset_view(request):
	context ={}

	# creating a formset and 5 instances of GeeksForm
	GeeksFormSet = modelformset_factory(GeeksModel, fields =['title', 'description'], extra = 3)
	formset = GeeksFormSet()

			
	# Add the formset to context dictionary
	context['formset']= formset
	return render(request, "home.html", context)


# get datetime
import datetime

# create a function
def geeks_view(request):
	# fetch date and time
	now = datetime.datetime.now()
	# convert to string
	html = "Time is {}".format(now)
	# return response
	return HttpResponse(html)


#------ function based view -----#
def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)


def list_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = GeeksModel.objects.all()
		
	return render(request, "list_view.html", context)


# pass id attribute from urls
def detail_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["data"] = GeeksModel.objects.get(id = id)
		
	return render(request, "detail_view.html", context)


#--- function based update view
from django.shortcuts import (get_object_or_404,
							render,
							HttpResponseRedirect)

# after updating it will redirect to detail_View
def detail_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["data"] = GeeksModel.objects.get(id = id)
		
	return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# fetch the object related to passed id
	obj = get_object_or_404(GeeksModel, id = id)

	# pass the object as instance in form
	form = GeeksForm(request.POST or None, instance = obj)

	# save the data from the form and
	# redirect to detail_view
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)

	# add form dictionary to context
	context["form"] = form

	return render(request, "update_view.html", context)


#------- function based delete view ------#
from django.shortcuts import (get_object_or_404,
							render,
							HttpResponseRedirect)
# delete view for details
def delete_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# fetch the object related to passed id
	obj = get_object_or_404(GeeksModel, id = id)


	if request.method =="POST":
		# delete object
		obj.delete()
		# after deleting redirect to
		# home page
		return HttpResponseRedirect("/")

	return render(request, "delete_view.html", context)


#------ class based view -----#

class GeeksList(ListView):

	# specify the model for list view
	model = GeeksModel

class MyView(View):
	def get(self, request):
		# <view logic>
		return HttpResponse('result')

class GeeksCreate(CreateView):

	# specify the model for create view
	model = GeeksModel

	# specify the fields to be displayed

	fields = ['title', 'description']

class GeeksDetailView(DetailView):
	# specify the model to use
	model = GeeksModel

class GeeksUpdateView(UpdateView):
	# specify the model you want to use
	model = GeeksModel

	# specify the fields
	fields = [
		"title",
		"description"
	]

	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="/"


class GeeksDeleteView(DeleteView):
	# specify the model you want to use
	model = GeeksModel
	
	# can specify success url
	# url to redirect after successfully
	# deleting object
	success_url ="/"


class GeeksFormView(FormView):
	# specify the Form you want to use
	form_class = GeeksForm
	
	# specify name of template
	template_name = "geeks / geeksmodel_form.html"

	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="/thanks/"

#
class GeeksWithFiledList(ListView):

	# specify the model for list view
	model = GeeksWithFieldModel

class GeeksWithFieldCreate(CreateView):

	# specify the model for create view
	model = GeeksWithFieldModel

	# specify the fields to be displayed

	fields = ['geeks_field']