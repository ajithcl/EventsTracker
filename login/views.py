from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    return render(request, 'login.html')


def verify_login(request):
    # Get the input username and password 
    login_name = request.GET.get ('login_name','')
    login_password = request.GET.get('login_password','')

    # Validate input user credentials 
    user = authenticate (username=login_name, password=login_password)

    if user is None:
        return JsonResponse ({'result':'error'})
    else:
        request.session['logged_user']=user.get_username()
        return JsonResponse({'result':'success'})