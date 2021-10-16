from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.entities),
    path('create_entity', views.create_entity),
    path('get_entities', views.get_entity_details),
]
