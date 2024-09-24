from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="activity"),
    path('create/', views.create, name="ActivityForm")
]
