from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('foundation-calc/', views.foundation_calc, name='foundation_calc'),
    path('floor-area-calc/', views.floor_area_calc, name='floor_area_calc'),
]
