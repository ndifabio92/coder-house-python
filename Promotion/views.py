from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(req):
    promotions = Promotion.objects.all()
    return render(req, "promotion/index.html",{
        "promotions": promotions
    })

def create(req):
    if(req.method == "POST"):
        form = PromotionForm(req.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_promotion = Promotion(
                first_activity=data['first_activity'],
                second_activity=data['second_activity'],
                discount_price=data['discount_price'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                is_active=data['is_active'],
            )
            new_promotion.save()
            return redirect('promotion')
    else:
        form = PromotionForm()

    return render(req, 'promotion/create.html', {'form': form})
