from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse


# Create your views here.
def entities(request):
    return render(request, 'entities.html')
