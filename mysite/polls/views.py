# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html')
def time(request):
    return HttpResponse("Welcome to Times of India page")
def home(request):
    a_list=Question.objects
    return render(request, 'base.html')
