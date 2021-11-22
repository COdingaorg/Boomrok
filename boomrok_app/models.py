from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import FileExtensionValidator
import datetime as dt
from django.utils.timezone import now as dt_now

# Create your models here.
class User_Subscribers(models.Model):
    '''
    details of users who have purchased a link to a movie
    '''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    #subscription_status = models.TextChoices()

class Movie(models.Model):
    '''
    Main movie, release date is the date movie will start showing, date posted is the date the file was uploaded
    '''
    movie_number = models.CharField(unique=True, max_length=100)
    title = models.CharField(unique = True, max_length=50)
    sub_title = models.TextField()
    poster = models.ImageField(upload_to = 'Files/Posters/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    movie_info = models.TextField()
    subscribers = models.ManyToManyField(to=User_Subscribers)
    release_date = models.DateTimeField(default=dt_now)
    date_posted = models.DateTimeField(default=dt_now, blank=False)
    movie_item = models.FileField(upload_to='Files/Movies/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

class Cast_Members(models.Model):
    '''
    Actors on a given movie. If an actor is availbale on multiple movies, entries have to be made individually
    '''
    image = models.ImageField(upload_to = 'Files/Cast_Members/')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    screen_name = models.CharField(max_length=35)
    role = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=CASCADE)

class Trailer(models.Model):
    '''
    Trailer models, related to movie, marking active on display means it displays on homepage
    '''
    active_on_display = models.BooleanField(default=False, unique=True)
    trailer_title = models.CharField(max_length=100)
    trailer_description = models.TextField()
    trailer_item = models.FileField(upload_to='Files/Trailers/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    date_posted = models.DateTimeField(default=dt_now, blank=False)
    movie = models.ForeignKey(Movie, on_delete=CASCADE, blank=True)