from django.shortcuts import render

# Create your views here.
site_name = 'Boomrok'
def index(request):
    '''
    view function rendering index page
    '''
    context={
        site_name : 'title',
    }
    return(request, context, 'user/home.html')