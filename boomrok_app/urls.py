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
  path('<int:pk>/', views.TrailerDetails.as_view(), name = 'trailer_details'),
  ]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)