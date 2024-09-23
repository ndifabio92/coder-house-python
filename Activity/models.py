from django.db import models
from django.db.models import Q
from decimal import Decimal
from typing import List

class Activity(models.Model):
    name: str = models.CharField(max_length=255)
    description: str = models.TextField()
    is_active: bool = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    def create_activity_price(activity: 'Activity', price: Decimal) -> 'Activity':
        if activity.is_active:
            new_activity = ActivityPrice.objects.create(activity=activity, price=price)
            return new_activity
        else:
            raise ValueError("La actividad no está activa.")

    def update_activity_price(activity: 'Activity', new_price: Decimal) -> 'Activity':
        if not activity.is_active:
            raise ValueError("La actividad no está activa.")
        
        update_activity = ActivityPrice.objects.filter(activity=activity, end_date__isnull=True).first()
        if update_activity:
            update_activity.end_date = timezone.now().date()
            update_activity.save()
        
        return update_activity

    def all() -> List['Activity']:
        return Activity.objects.prefetch_related('prices').all()
    
    def find(search_params: str) -> List['Activity']:
        try:
            # Buscar por ID si el término es numérico
            if search_term.isdigit():
                return Activity.objects.filter(id=search_term)
            
            # Buscar por nombre (ignorando mayúsculas/minúsculas)
            return Activity.objects.filter(Q(name__iexact=search_term))
        except Activity.DoesNotExist:
            return None
    
    def current_price(self) -> Decimal:
        latest_price = self.prices.filter(end_date__isnull=True).first()
        return latest_price.price if latest_price else None


class ActivityPrice(models.Model):
    activity = models.ForeignKey(Activity, related_name='prices', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.activity.name} - {self.price}"
