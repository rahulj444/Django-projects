from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    s='<h6>Rahul Balijapally </h6>'

    return HttpResponse(s)

# Create your views here.
