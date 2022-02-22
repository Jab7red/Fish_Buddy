from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fishes/', views.fishes_index, name='fishes_index'),
    path('fishes/<int:fish_id>/', views.fish_detail, name='fish_detail'),
    path('fishes/create/', views.FishCreate.as_view(), name='fishes_create'),
    path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fishes_update'),
    path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fishes_delete'),
    path('gears/', views.gears_index, name='gears_index'),
    path('gears/<int:gear_id>/', views.gear_detail, name='gear_detail'),
    path('gears/create/', views.GearCreate.as_view(), name='gears_create'),
    path('gears/<int:pk>/update/', views.GearUpdate.as_view(), name='gears_update'),
    path('gears/<int:pk>/delete/', views.GearDelete.as_view(), name='gears_delete'),
    path('fishes/<int:fish_id>/add_lake/', views.add_lake, name='add_lake'),
    path('fishes/<int:fish_id>/assoc_gear/<int:gear_id>/', views.assoc_gear, name='assoc_gear'),
    path('fishes/<int:fish_id>/add_log/', views.add_log, name='add_log'),
    path('accounts/signup/', views.signup, name='signup'),
]