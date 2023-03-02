from django.urls import path
from .views import get_printer_all

urlpatterns = [
    path('all/', get_printer_all, name="get_printers_all"),

]
