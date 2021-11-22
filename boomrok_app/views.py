from django.contrib.admin.sites import site
from django.shortcuts import render

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