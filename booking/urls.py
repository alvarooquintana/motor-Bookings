from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.index, name='index'),
]