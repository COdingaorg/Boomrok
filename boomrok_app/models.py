from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.
class User_Subscribers(models.Model):
    '''
    details of users who have purchased a link to a movie
    '''
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    #subscription_status = models.TextChoices()

class Movie(models.Model):
    '''
    Main movie, marking active on display means it displays on homepage
    '''
    movie_number = models.CharField(unique=True, max_length=100)
    title = models.CharField(unique = True, max_length=50)
    sub_title = models.TextField()
    poster = models.ImageField(upload_to = 'Posters/')
    active_on_display = models.BooleanField(default=False, unique=True)
    movie_info = models.TextField()
    subscribers = models.ManyToManyField(to=User_Subscribers)
    movie_item = models.TextField()

class Cast_Members(models.Model):
    '''
    Actors on a given movie
    '''
    image = models.ImageField(upload_to = 'Cast_Members/')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    screen_name = models.CharField(max_length=35)
    role = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=CASCADE)

class Trailer(models.Model):
    '''
    Trailer models, related to movie
    '''
    trailer_title = models.TextField()
    trailer_item = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=CASCADE)


