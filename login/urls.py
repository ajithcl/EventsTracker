from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
                  path('', views.login),
                  path('login/verify_login', views.verify_login),
                  path ('logout', views.logout),
              ] 