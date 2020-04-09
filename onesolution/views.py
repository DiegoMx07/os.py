from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def date (request):
	date=datetime.datetime.now()

	return HttpResponse(date)

def calculated (request, edad, agno):
	periodo=agno-2020
	edadfutura=edad+periodo
	vista=edadfutura

	return HttpResponse(vista)




def home (request): #vista home

	return render(request, "home.html")

def services(request): #vista servicios
	
	return render(request, "services.html")

def about (request): #vista acerca de

	return render(request, "about.html")