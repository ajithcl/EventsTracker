########################
# EVENTS VIEW          #
########################

from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Event
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import datetime
from .functions import handle_uploaded_file


# Create your views here.

def display_events(request):
    entity_name = request.GET.get('entityname')
    user_id = request.session['logged_user']

    return render(request, 'events.html')


# TODO
@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        login_name = request.session['logged_user']
        input_entity_name = request.POST.get('entity_name', '')
        input_event_name = request.POST.get('event_name', '')
        input_comments = request.POST.get('comments', '')

        if len(request.FILES) > 0:
            image_file = request.FILES['image_path']
            uploaded_image_name = handle_uploaded_file(image_file)
            if uploaded_image_name is None:
                uploaded_image_name = ''
        else:
            uploaded_image_name = ''

        event_object = Event.objects.create(EventDate=datetime.date.today(),
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


# TODO
def get_event_details(request):
    pass
