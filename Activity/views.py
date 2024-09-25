from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home(req):
    activities = Activity.objects.all()
    return render(req, "activity/index.html", {
        "activities": activities
    })

def create(req):
    if(req.method == 'POST'):
        form = ActivityForm(req.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            new_activity = Activity(
                name=data['name'],
                description=data['description']
            )
            new_activity.create_activity_price(data['price'])
            return redirect('activity')
    else:
        form = ActivityForm()
    
    return render(req, 'activity/create.html', {'form': form})

def price(req):
    activities_prices = ActivityPrice.objects.all()
    return render(req, "activity_price/index.html", {
        "activities_prices": activities_prices
    })

def search(req):
    search_value = req.GET.get('search_value')
    results = Activity.find(search_value)

    return render(req, "activity/index.html", {
        "activities": results
    })