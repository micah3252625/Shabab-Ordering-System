
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order-tracker/', views.orderTracker, name='orderTracker'),
]
