from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.entities),
                  path('create_entity', views.create_entity),
                  path('get_entities', views.get_entity_details),
              ]
