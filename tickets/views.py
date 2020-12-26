from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    http="<h2>Welcome to the Hypercar Service!</h2>"
    return HttpResponse(http)