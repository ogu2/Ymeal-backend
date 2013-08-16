# Create your views here.
try: import simplejson as json
except ImportError: import json
import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from models import Cafeteria, Attribute, Serving, Meal, Reaction, YUser

from django.core.paginator import Paginator
# General Fns
def meal_selector(className, request=None):
    data = [item.prepare() for item in className.objects.all()]
    return HttpResponse(json.dumps(data),content_type="application/json")

def pre_process(className, data):
    if className.__name__ == "Serving":
        data = data.filter(date = datetime.datetime.now().date() )
    return data

def all_selector(className):
    data = [item.prepare() for item in pre_process(className, className.objects.all())]
    return HttpResponse(json.dumps(data),content_type="application/json")

def id_selector(request, className):
    _id = request.GET.get('id')
    info = {}
    if _id:
        info = className.objects.filter(id=int(_id))
    return HttpResponse(json.dumps(info),content_type="application/json")

#---------- Dining Halls
#/api/halls
def all_halls(request):
    return all_selector(Cafeteria)

#/api/hall/(id)
def hall_info(request):
    return id_selector(request, Cafeteria)

#---------- Meals

#/api/meal/(id)
def meal_info(request):
    return id_selector(request, Meal)

#----------Meal (dis)likes
def reaction_process(request,meal_id,custom_reaction):
    print custom_reaction
    device_id = request.POST.get('device_id')
    if not device_id:
        return HttpResponse('No device_id')
    _serving = Serving.objects.filter(pk=meal_id)
    if not _serving:
        return HttpResponse('Meal not found')
    else:
        _serving= _serving[0]
    if type(device_id) is list:
        device_id = str(device_id[0])
    else:
        device_id = str(device_id)
    yuser = YUser.objects.get_or_create(
             device_id =str(device_id)
            )[0]
    # save reaction
    try:
        Reaction.objects.get(
                user = yuser,
                serving = _serving,
                feedback = int(custom_reaction)
                )
    except:
        Reaction(
                user = yuser,
                serving = _serving,
                feedback = int(custom_reaction)
                ).save()
    return HttpResponse('OK')

def like_serving(request, meal_id):
    return reaction_process(request,meal_id,Reaction.LIKE)

def dislike_serving(request, meal_id):
    return reaction_process(request,meal_id,Reaction.DISLIKE)

#----------Servings
#/api/meals
def todays_servings(request):
    return all_selector(Serving)

#---------- Comments
#/api/meal/comments
#/api/comment/(id)
#---------- YUser
#/api/user/(id)

