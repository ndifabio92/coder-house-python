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