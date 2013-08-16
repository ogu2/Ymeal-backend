# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

def home(request):
    return render_to_response('page.html')

def dummy(request):
    info = [{'attributes': ['vegan', 'yummy'],
      'cafeteria': 'urls',
      'date': '08/01/2013',
      'description': 'veru long desciption',
      'id': 1,
      'name': 'some name'},
     {'attributes': ['vegan', 'yummy'],
      'cafeteria': 'building e',
      'date': '08/01/2013',
      'description': 'veru long desciption',
      'id': 2,
      'name': 'some name two'},
     {'attributes': ['vegan', 'yummy'],
      'cafeteria': 'building f',
      'date': '08/01/2013',
      'description': 'veru long desciption',
      'id': 3,
      'name': 'some name three'}]
    return HttpResponse(json.dumps(info),content_type="application/json")
