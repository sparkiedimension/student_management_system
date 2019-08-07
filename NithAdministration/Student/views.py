from django.shortcuts import render
from .models import Student,Suggestions
from django.shortcuts import render, redirect
from django.views.generic import ListView

def index(request):
    return render(request, 'layout1.html')

def guidelines(request):
    return render(request, 'guidelines.html')

def staffguidelines(request):
    return render(request, 'staffguidelines.html')





