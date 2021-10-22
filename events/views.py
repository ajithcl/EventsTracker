########################
# EVENTS VIEW          #
########################

from django.shortcuts import render
from .models import Event
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import datetime
from .functions import handle_uploaded_file
from django.core import serializers


# Create your views here.

def display_events(request):
    entity_name = request.GET.get('entityname')
    args = {'entity_name': entity_name}

    return render(request, 'events.html', args)


@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        login_name = request.session['logged_user']
        input_entity_name = request.POST.get('entity_name', '')
        input_event_name = request.POST.get('event_name', '')
        input_event_date = request.POST.get('event_date', datetime.date.today())
        input_comments = request.POST.get('comments', '')

        if len(request.FILES) > 0:
            image_file = request.FILES['image_path']
            uploaded_image_name = handle_uploaded_file(image_file)
            if uploaded_image_name is None:
                uploaded_image_name = ''
        else:
            uploaded_image_name = ''

        event_object = Event.objects.create(EventDate=input_event_date,
                                            EntityName=input_entity_name,
                                            EventName=input_event_name,
                                            Comments=input_comments,
                                            UserId=login_name,
                                            ImageFileName=uploaded_image_name
                                            )
        if event_object is None:
            return JsonResponse({'result': 'error',
                                 'comments': 'Event not created.'})
        else:
            return JsonResponse({'result': 'success',
                                 'comments': 'Event created'})
    else:
        return JsonResponse({'result': 'error',
                             'comments': 'Not a POST method'})


def get_event_details(request):
    if request.method == 'GET':
        login_name = request.session['logged_user']
        entity_name = request.GET.get('entity_name')

        event_list = Event.objects.filter(UserId=login_name, EntityName=entity_name)
        event_list = serializers.serialize('json', event_list)
        return JsonResponse({'result': 'success',
                             'data': event_list})
    else:
        return JsonResponse({'result': 'error',
                             'comments': ' Not a GET method'})
