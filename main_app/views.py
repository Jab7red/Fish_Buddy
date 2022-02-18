from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


#======
# HOME
#======
def home(request):
    return HttpResponse('<h1>Home Page Coming Soon</h1>')

#======
# ABOUT
#======
def about(request):
    return render(request, 'about.html')