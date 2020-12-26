from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        http="<h2>Welcome to the Hypercar Service!</h2>"
        return HttpResponse(http)        