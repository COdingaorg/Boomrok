from django.urls import reverse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Movie, Trailer

# Create your views here.
site_name = 'Boomrok'
def index(request):
    '''
    view function rendering index page
    '''
    context = {
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

class UploadMovie(CreateView):
    '''
    create view for uploading movies
    '''
    model = Movie
    fields = ['movie_number','title', 'sub_title', 'poster', 'movie_info', 'release_date', 'movie_item']
    template_name = 'admin/movie_upload.html'

    def get_success_url(self):
        return reverse('trailer_upload')