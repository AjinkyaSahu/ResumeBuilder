from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def Home(request):

    return HttpResponse("Welcome to the home page")
