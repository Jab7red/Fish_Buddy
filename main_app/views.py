from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Fish


# Create your views here.

#======
# HOME
#======
def home(request):
    return render(request, 'home.html')

#======
# ABOUT
#======
def about(request):
    return render(request, 'about.html')

#===========
# Fish Index
#===========
def fishes_index(request):
    fishes = Fish.objects.all()
    return render(request, 'fishes/index.html', { 'fishes': fishes })

#============
# Fish Detail
#============
def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fishes/detail.html', { 'fish': fish })

#============
# Fish Create
#============
class FishCreate(CreateView):
    model = Fish
    fields = '__all__'