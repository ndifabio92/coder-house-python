from django.contrib import admin
from .models import Promotion

class PromotionAdmin(admin.ModelAdmin):
    list_display = ('first_activity', 'second_activity', 'discount_price', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')

admin.site.register(Promotion, PromotionAdmin)