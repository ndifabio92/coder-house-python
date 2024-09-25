from django.db import models
from decimal import Decimal
from django.utils import timezone
from Activity.models import Activity

class Promotion(models.Model):
    first_activity = models.ForeignKey(Activity, related_name='promotions1', on_delete=models.CASCADE)
    second_activity = models.ForeignKey(Activity, related_name='promotions2', on_delete=models.CASCADE)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Promo: {self.first_activity.name} & {self.second_activity.name} - Precio: {self.discount_price}"

    def isActive(self) -> bool:
        now = timezone.now().date()
        return self.is_active and self.start_date <= now and (self.end_date is None or self.end_date >= now)

    def are_activities_active(self) -> bool:
        return self.first_activity.is_active and self.second_activity.is_active

    def updatePrice(self, new_price: Decimal):
        if new_price < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.discount_price = new_price

        # if self.first_activity == self.second_activity:
        #     raise ValidationError("Las actividades no pueden ser las mismas.")

        self.save()
