from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def display_events(request):
    return render(request, 'events.html')
