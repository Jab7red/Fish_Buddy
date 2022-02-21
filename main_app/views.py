from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish, Gear
from .forms import LakeForm


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
    gears_fish_doesnt_have = Gear.objects.exclude(id__in = fish.gears.all().values_list('id'))
    lake_form = LakeForm()
    return render(request, 'fishes/detail.html', { 'fish': fish, 'lake_form': lake_form, 'gears': gears_fish_doesnt_have })

#=========
# Add Lake
#=========
def add_lake(request, fish_id):
    form = LakeForm(request.POST)
    if form.is_valid():
        new_lake = form.save(commit=False)
        new_lake.fish_id = fish_id
        new_lake.save()
    return redirect('fish_detail', fish_id=fish_id)

#==============
# Assocociation
#==============
def assoc_gear(request, fish_id, gear_id):
    Fish.objects.get(id=fish_id).gears.add(gear_id)
    return redirect('fish_detail', fish_id=fish_id)

#============
# Fish Create
#============
class FishCreate(CreateView):
    model = Fish
    fields = ('name', 'image')

#============
# Fish Update
#============
class FishUpdate(UpdateView):
    model = Fish
    fields = ('name', 'image')

#============
# Fish Delete
#============
class FishDelete(DeleteView):
    model = Fish
    success_url = '/fishes/'

#===========
# Gear Index
#===========
def gears_index(request):
    gears = Gear.objects.all()
    return render(request, 'gears/index.html', { 'gears': gears})

#============
# Gear Detail
#============
def gear_detail(request, gear_id):
    gear = Gear.objects.get(id=gear_id)
    return render(request, 'gears/detail.html', { 'gear': gear })

#============
# Gear Create
#============
class GearCreate(CreateView):
    model = Gear
    fields = ('name', 'color')

#============
# Gear Update
#============
class GearUpdate(UpdateView):
    model = Gear
    fields = ('name', 'color')

#============
# Gear Delete
#============
class GearDelete(DeleteView):
    model = Gear
    success_url = '/gears/'
