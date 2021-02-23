from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-price').filter(is_featured=True)
    all_cars = Car.objects.order_by('-price')
    year_search = Car.objects.order_by('year').values('year').distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'year_search' : year_search,
    }
    return render(request,'pages/home.html',data)

def about(request):
    return render(request,'pages/about.html')

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')
