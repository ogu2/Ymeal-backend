from django.conf.urls import patterns, include, url
from api import views

urlpatterns = patterns('',
    url(r'^$', 'mealer.views.home', name='home'),
#----------Meal
    url(r'^meals/$', views.todays_servings),
    url(r'^meals/(?P<meal_id>\d+)/like$', views.like_serving),
    url(r'^meals/(?P<meal_id>\d+)/dislike$', views.dislike_serving),
)
