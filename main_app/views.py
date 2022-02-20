from django.shortcuts import render


# Create your views here.

class Fish:
    def __init__(self, name, image):
        self.name = name
        self.image = image

fishes = [
    Fish('Largemouth Bass', 'https://bcinvasives.ca/wp-content/uploads/2021/01/Largemouth-Bass_001_wetaworm.com_-600x400.jpg'),
    Fish('Smallmouth Bass', 'https://www.nps.gov/obed/learn/nature/images/bass-285.jpg'),
    Fish('Catfish', 'https://farm66.staticflickr.com/65535/5569680777_511cb14967_b.jpg')
]


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
    return render(request, 'fishes/index.html', { 'fishes': fishes })