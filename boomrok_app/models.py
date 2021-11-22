from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.core.validators import FileExtensionValidator
from Boomrok_project.settings import TIME_ZONE

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
    Main movie, marking active on display means it displays on homepage
    '''
    movie_number = models.CharField(unique=True, max_length=100)
    title = models.CharField(unique = True, max_length=50)
    sub_title = models.TextField()
    poster = models.ImageField(upload_to = 'Files/Posters/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    active_on_display = models.BooleanField(default=False, unique=True)
    movie_info = models.TextField()
    subscribers = models.ManyToManyField(to=User_Subscribers)
    release_date = models.DateTimeField()
    date_posted = models.DateTimeField(default=TIME_ZONE.now)
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
    Trailer models, related to movie
    '''
    trailer_title = models.TextField()
    trailer_item = models.FileField(upload_to='Files/Trailers/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    movie = models.ForeignKey(Movie, on_delete=CASCADE)


