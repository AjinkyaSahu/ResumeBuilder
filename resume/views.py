from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def resumeHome(request):

    return HttpResponse("Hello, world. Resume.")
    # return render()
