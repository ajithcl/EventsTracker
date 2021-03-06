from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_events),
    path('create_event', views.create_event),
    path('get_events', views.get_event_details)
]
