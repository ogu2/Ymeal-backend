from django.db import models

# Create your models here.
class DiningHall(models.Model):
    """This will be one of the A-G dining halls"""
    name = models.CharField(max_length=200)

class Meal(models.Model):
    """Single meal eg. fries with kattofeln
    contains info on likes and dislikes"""
    name = models.CharField(max_length=200)
    dhall = models.ForeignKey('DiningHall')
    date = models.DateField(null=True)
    descr = models.CharField(max_length=1000)

class YUser(models.Model):
    """(Yahoo!) employee who uses app"""
    device_id = models.CharField(max_length=100, null=True)
    # TODO: Decide if we want to add more info

class Comment(models.Model):
    """User comment"""
    user = models.ForeignKey('YUser', blank=True, null=True)
    comment = models.CharField(max_length=250)
