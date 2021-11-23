from django.urls import reverse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Cast_Members, Movie, Trailer
from boomrok_app import models

# Create your views here.
site_name = 'Boomrok'
def index(request):
    '''
    view function rendering index page
    '''

    home_display = Trailer.objects.filter(active_on_display = True).last()
    cast_members = Cast_Members.objects.filter(movie = home_display.movie.pk).all()
    
    context = {
        'cast_members':cast_members,
        'now_trailer': home_display,
        'title':f"{site_name}-Home"
    }
    return render(request,'user/home.html', context)

class CreateTrailer(CreateView):
    model = Trailer
    fields = ['trailer_title','trailer_description', 'trailer_item', 'movie', 'active_on_display']
    template_name = 'admin/trailer_upload.html'

    def get_success_url(self):
        return reverse('trailer_details', kwargs={'pk':self.object.pk})

class TrailerDetails(DetailView):
    model = Trailer
    template_name = 'user/trailer_details.html'

class UpdateTrailer(UpdateView):
    model = Trailer
    fields = ['trailer_title', 'trailer_description', 'movie', 'active_on_display']
    template_name = 'admin/trailer_upload.html'

    def get_success_url(self):
        return reverse('trailer_details', kwargs={'pk':self.object.pk})



class UploadMovie(CreateView):
    '''
    create view for uploading movies
    '''
    model = Movie
    fields = ['movie_number','title', 'sub_title', 'poster', 'movie_info', 'release_date', 'movie_item']
    template_name = 'admin/movie_upload.html'

    def get_success_url(self):
        return reverse('trailer_upload')

class MovieDetails(DetailView):
    '''
    view Moview details, watch movie
    '''
    model = Movie
    template_name = 'user/movie_details.html'
class UpdateMovie(UpdateView):
    '''
    updates movie details
    '''
    model = Movie
    fields = ['title', 'sub_title', 'poster', 'movie_info','release_date']
    template_name = 'admin/movie_upload.html'

    def get_success_url(self):
        return reverse('movie_details', kwargs={'pk':self.object.pk})

class DeleteMovie(DeleteView):
    '''
    Deletes a selected movie item
    '''
    model = Movie
    template_name = 'admin/delete_item.html'

    def get_success_url(self):
        return reverse('index')

class CreateCast(CreateView):
    '''
    Creates cast members
    '''
    model = Cast_Members
    fields = ['first_name', 'last_name', 'screen_name', 'role','image', 'movie']
    template_name = 'admin/create_cast.html'

    def get_success_url(self):
        return reverse('create_cast') 