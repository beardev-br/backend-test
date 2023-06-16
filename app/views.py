from django.shortcuts import render, redirect
from app.forms import CarsForm
from app.models import Cars
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cars.objects.filter(Q(id__icontains=search)|Q(car_color__icontains=search)|Q(license_plate__icontains=search))     
    else:
        data['db'] = Cars.objects.all()
    #all = Cars.objects.all()
    #paginator = Paginator(all, 3)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    print(data)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarsForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Cars.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cars.objects.get(pk=pk)
    data['form'] = CarsForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cars.objects.get(pk=pk)
    form = CarsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Cars.objects.get(pk=pk)
    db.delete()
    return redirect('home')