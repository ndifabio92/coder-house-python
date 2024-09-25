from django.contrib import admin
from .models import *

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_price', 'is_active')
    search_fields = ('name',)


class ActivityPriceAdmin(admin.ModelAdmin):
    list_display = ('activity', 'price', 'start_date', 'end_date')
    list_filter = ('activity', 'start_date')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityPrice, ActivityPriceAdmin)