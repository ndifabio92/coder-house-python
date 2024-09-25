from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="promotion"),
    path('create/', views.create, name="PromotionForm")
]
