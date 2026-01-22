from django.urls import path
from .views import trader_dashboard

urlpatterns = [
    path("dashboard/", trader_dashboard),
]
