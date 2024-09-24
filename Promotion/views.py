from django.shortcuts import render
from .models import *

# Create your views here.

def home(req):
    promotions = Promotion.objects.all()
    return render(req, "promotion/index.html",{
        "promotions": promotions
    })