from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="activity"),
    path('create/', views.create, name="ActivityForm"),
    path('price/', views.price, name="activity_price"),
    path('search/', views.search, name='activity_search'),
]
