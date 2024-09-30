from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Привет джанго')

def list_students(request):
    return HttpResponse('list_students')


def list_groups(request):
    return HttpResponse('list_groups')