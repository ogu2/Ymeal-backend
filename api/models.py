from django.db import models

# Create your models here.
class DiningHall(models.Model):
    """This will be one of the A-G dining halls"""
    name = models.CharField(max_length=200)

class Attribute(models.Model):
    """Is the meal vegeterian, gluten free etc."""
    description = models.CharField(max_length=100)

class Meal(models.Model):
    """Single meal eg. fries with kattofeln
    contains info on likes and dislikes"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    attributes = models.ManyToManyField(Attribute)

class Serving(models.Model):
    """An instance when a meal is served"""
    meal = models.ForeignKey(Meal)
    location = models.ForeignKey(DiningHall)
    date = models.DateField(null=True, blank=True)

    # choices: django docs /ref/models/fields.html
    BREAKFAST='BR'
    LUNCH='LN'
    DINNER='DN'
    TIME_CHOICES = (
            (BREAKFAST,'Breakfast'),
            (LUNCH, 'Lunch'),
            (DINNER, 'Dinner'),
            )
    time_of_day = models.CharField(max_length=2,
                                      choices=TIME_CHOICES,
                                      default=LUNCH)

class YUser(models.Model):
    """(Yahoo!) employee who uses app"""
    device_id = models.CharField(max_length=100)
    # TODO: Decide if we want to add more info

class Comment(models.Model):
    """User comment"""
    user = models.ForeignKey('YUser', blank=True, null=True)
    comment = models.CharField(max_length=250)

class Reaction(models.Model):
    """A Yuser's reaction to the meal for a particular
    serving. This enables us to track days when users
    like a meal they otherwise hate or vice versa"""
    LIKE=1
    DISLIKE=2
    NEITHER=3
    REACTION_CHOICES = (
            (LIKE,'Like'),
            (DISLIKE,'Dislike'),
            (NEITHER,'Neither'),
            )
    user = models.ForeignKey(YUser)
    serving = models.ForeignKey(Serving)
    feedback = models.PositiveSmallIntegerField(choices=REACTION_CHOICES,
                                                default=NEITHER)

