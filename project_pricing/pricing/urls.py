from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/pricing/', views.calculate_ride_pricing, name="pricing-calc")
]