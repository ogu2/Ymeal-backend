from django.conf.urls import patterns, include, url
from api import views

urlpatterns = patterns('',
    url(r'^$', 'mealer.views.home', name='home'),
#----------Meal
    url(r'^meals/$', views.todays_servings),

)
