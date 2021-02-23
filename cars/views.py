from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars,2)
    page = request.GET.get('page')
    paged = paginator.get_page(page)
    data = {
        'cars': paged,
    }
    return render(request,'cars/cars.html',data)

def car_detail(request,id):
    single_car = get_object_or_404(Car,pk=id)
    data = {
        'single_car':single_car,
    }
    return render(request,'cars/car_detail.html',data)

def search(request):
    cars = Car.objects.all()

    if request.GET['keyword']:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_name__icontains = keyword)

    if request.GET['year_search']:
        year_search = request.GET['year_search']
        if year_search:
            cars = cars.filter(year__iexact = year_search)


    data = {
        'cars' : cars,
    }
    return render(request,'cars/search.html',data)