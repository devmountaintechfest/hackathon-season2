from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch/', views.get_employees, name='get_employees'),
    path('load_init_employees_trigger/', views.load_init_employees_trigger, name='load_init_employees_trigger')
]