from django.db import models

# Create your models here.

class Cafeteria(models.Model):
    """This will be one of the A-G dining halls"""
    name = models.CharField(max_length=200)

    def prepare(self):
        return self.name

    def __unicode__(self):
        return self.name

class Attribute(models.Model):
    """Is the meal vegeterian, gluten free etc."""
    description = models.CharField(max_length=100)

    def prepare(self):
        return self.description

    def __unicode__(self):
        return self.description


class Meal(models.Model):
    """Single meal eg. fries with kattofeln
    contains info on likes and dislikes"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    attributes = models.ManyToManyField(Attribute, blank=True, null=True)

    def prepare(self):
        return {
                'meal_id': self.pk,
                'name':self.name,
                'description':self.description,
                'attributes' : [x.prepare() for x in self.attributes.all()]
                }

    def __unicode__(self):
        attrs = ','.join([a.description for a in self.attributes.all()])
        return str(self.name)+'('+attrs+')' if attrs else str(self.name)

class Serving(models.Model):
    """An instance when a meal is served"""
    meal = models.ForeignKey(Meal)
    location = models.ForeignKey(Cafeteria)
    date = models.DateField(null=True, blank=True)

    # choices: django docs /ref/models/fields.html
    BREAKFAST = 'BR'
    LUNCH = 'LN'
    DINNER = 'DN'
    TIME_CHOICES = (
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    )
    time_of_day = models.CharField(max_length=2,
                                   choices=TIME_CHOICES,
                                   default=LUNCH)
    def prepare(self):
        x= {
                'cafeteria':self.location.prepare(),
                'category':'pizza',
                'date':str(self.date)
                }
        y = self.meal.prepare()
        return dict(x.items()+y.items())
    def __unicode__(self):
        return str(self.meal) + ' at '+str(self.location)+' on '+str(self.date)
#class YUser(models.Model):
#    """(Yahoo!) employee who uses app"""
#    device_id = models.CharField(max_length=100)
#    # TODO: Decide if we want to add more info
#
#
#class Comment(models.Model):
#    """User comment"""
#    user = models.ForeignKey('YUser', blank=True, null=True)
#    comment = models.CharField(max_length=250)
#
#
#class Reaction(models.Model):
#    """A Yuser's reaction to the meal for a particular
#    serving. This enables us to track days when users
#    like a meal they otherwise hate or vice versa"""
#    LIKE = 1
#    DISLIKE = 2
#    NEITHER = 3
#    REACTION_CHOICES = (
#        (LIKE, 'Like'),
#        (DISLIKE, 'Dislike'),
#        (NEITHER, 'Neither'),
#    )
#    user = models.ForeignKey(YUser)
#    serving = models.ForeignKey(Serving)
#    feedback = models.PositiveSmallIntegerField(choices=REACTION_CHOICES,
#                                                default=NEITHER)
