from django.shortcuts import render
from .models import Booking


def index(request, email, phone):
    
        return render(
            request, 'index.html'
        )
        