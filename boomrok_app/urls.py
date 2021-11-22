from django.conf.urls import url
from django.views.generic.detail import DetailView
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^trailer_upload/$', views.CreateTrailer.as_view(), name = 'trailer_upload'),
  url(r'^movie_upload/$', views.UploadMovie.as_view(), name = 'movie_upload'),
  path('<int:pk>/edit_movie/', views.UpdateMovie.as_view(), name = 'edit_movie'),
  path('<int:pk>/trailer/', views.TrailerDetails.as_view(), name = 'trailer_details'),
  path('<int:pk>/edit_trailer/', views.UpdateTrailer.as_view(), name = 'edit_trailer'),
  path('<int:pk>/movie_details/', views.MovieDetails.as_view(), name = 'movie_details'),
  path('<int:pk>/delete_movie/', views.DeleteMovie.as_view(), name = 'Delete_movie')
  ]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)