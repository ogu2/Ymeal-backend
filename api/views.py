# Create your views here.
try: import simplejson as json
except ImportError: import json

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from models import DiningHall, Meal, YUSer, Comment

# General Fns
def all_selector(className)
    data = className.objects.all()
    return HttpResponse(json.dumps(data),content_type="application/json")

def id_selector(request, className):
    _id = request.GET.get('id')
    info = {}
    if _id:
        info = className.objects.filter(id=int(_id))
    return HttpResponse(json.dumps(info),content_type="application/json")

# Dining Halls

#/api/halls
def all_halls(request):
    return all_selector(DiningHall)

#/api/hall/(id)
def hall_info(request):
    return id_selector(request, DiningHall)

# Meals

#/api/meals
def all_meals(request):
    return all_selector(Meal)

#/api/meal/(id)
def meal_info(request):
    return id_selector(request, Meal)

# Comments

#/api/meal/comments

#/api/comment/(id)

# YUser

#/api/user/(id)
