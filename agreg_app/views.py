from django.shortcuts import render
from .models import Values
from .forms import LookValue
# Create your views here.


def index(request):
    return render(request, 'agreg_app/index.html')


def look(request):
    values = Values.objects.all()
    return render(request, 'agreg_app/look.html', {'values': values})


def look_closely(request):
    # form = LookValue
    values = Values.objects.all(filter())
    return render()


def add(request):

    return render(request, 'agreg_app/add.html')
