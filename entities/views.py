#########################
# Entities Views        #
#########################


from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Entity
import datetime
from .functions import handle_uploaded_file
from django.core import serializers


# Create your views here.
def entities(request):
    return render(request, 'entities.html')


@csrf_exempt
def create_entity(request):
    if request.method == 'POST':
        login_name = request.session['logged_user']
        input_entity_name = request.POST.get('entity_name', '')
        input_comments = request.POST.get('comments', '')

        if len(request.FILES) > 0:
            image_file = request.FILES['image_path']
            uploaded_image_name = handle_uploaded_file(image_file)
            if uploaded_image_name is None:
                uploaded_image_name = ''
        else:
            uploaded_image_name = ''

        entity_object = Entity.objects.create(EntityName=input_entity_name,
                                              CreatedDate=datetime.date.today(),
                                              UpdatedDate=datetime.date.today(),
                                              Comments=input_comments,
                                              ImageFileName=uploaded_image_name,
                                              UserId=login_name)

        if entity_object is None:
            return JsonResponse({'result': 'error',
                                 'comments': 'Entity not created.'})
        else:
            return JsonResponse({'result': 'success',
                                 'comments': 'Entity created.'})
    else:
        return JsonResponse({'result': 'error',
                             'comments': 'Not a POST method'})


def get_entity_details(request):
    if request.method == 'GET':
        login_name = request.session['logged_user']
        entity_list = Entity.objects.filter(UserId=login_name)
        entity_list = serializers.serialize('json', entity_list)
        return JsonResponse({'result': 'success',
                             'data': entity_list})
    else:
        return JsonResponse({'result': 'error',
                             'comments': 'Not a GET method'})
