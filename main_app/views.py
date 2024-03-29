from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Fish, Gear, Log
from .forms import LakeForm, LogForm


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

#========
# Sign up
#========
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('fishes_index')
        else:
            error_message = 'Invalid Sign Up - Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

#===========
# Fish Index
#===========
@login_required
def fishes_index(request):
    fishes = Fish.objects.filter(user=request.user)
    return render(request, 'fishes/index.html', { 'fishes': fishes })

#============
# Fish Detail
#============
@login_required
def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    gears_fish_doesnt_have = Gear.objects.exclude(id__in = fish.gears.all().values_list('id'))
    lake_form = LakeForm()
    log_form = LogForm()
    return render(request, 'fishes/detail.html', { 
        'fish': fish, 
        'lake_form': lake_form, 
        'gears': gears_fish_doesnt_have,
        'log_form': log_form 
    })

#=========
# Add Lake
#=========
@login_required
def add_lake(request, fish_id):
    form = LakeForm(request.POST)
    if form.is_valid():
        new_lake = form.save(commit=False)
        new_lake.fish_id = fish_id
        new_lake.save()
    return redirect('fish_detail', fish_id=fish_id)

#========
# Add Log
#========
@login_required
def add_log(request, fish_id):
    form = LogForm(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.fish_id = fish_id
        new_log.save()
    return redirect('fish_detail', fish_id=fish_id)

#==============
# Assocociation
#==============
@login_required
def assoc_gear(request, fish_id, gear_id):
    Fish.objects.get(id=fish_id).gears.add(gear_id)
    return redirect('fish_detail', fish_id=fish_id)

#============
# Fish Create
#============
class FishCreate(LoginRequiredMixin, CreateView):
    model = Fish
    fields = ('name', 'image')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#============
# Fish Update
#============
class FishUpdate(LoginRequiredMixin, UpdateView):
    model = Fish
    fields = ('name', 'image')

#============
# Fish Delete
#============
class FishDelete(LoginRequiredMixin, DeleteView):
    model = Fish
    success_url = '/fishes/'

#===========
# Gear Index
#===========
@login_required
def gears_index(request):
    gears = Gear.objects.all()
    return render(request, 'gears/index.html', { 'gears': gears})

#============
# Gear Detail
#============
@login_required
def gear_detail(request, gear_id):
    gear = Gear.objects.get(id=gear_id)
    return render(request, 'gears/detail.html', { 'gear': gear })

#============
# Gear Create
#============
class GearCreate(LoginRequiredMixin, CreateView):
    model = Gear
    fields = ('name', 'color')

#============
# Gear Update
#============
class GearUpdate(LoginRequiredMixin, UpdateView):
    model = Gear
    fields = ('name', 'color')

#============
# Gear Delete
#============
class GearDelete(LoginRequiredMixin, DeleteView):
    model = Gear
    success_url = '/gears/'
