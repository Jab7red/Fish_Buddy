from django.shortcuts import render
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