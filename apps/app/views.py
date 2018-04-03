from django.shortcuts import render, redirect


# Create your views here.

def index(request):
	return render (request, 'message.html')

def home(request):
	return render(request, 'index.html')

