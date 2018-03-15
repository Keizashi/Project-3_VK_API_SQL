from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Note
import requests
import json


# Create your views here.
def index(request):
    notes_dict = {
        "data": []
    }

    all_entries = Note.objects.all().order_by('-id')
    for entry in all_entries:
        dict_element = {
            "id": entry.id,
            "text": entry.text
            }
        notes_dict['data'].append(dict_element)
    return JsonResponse(notes_dict, safe=False)