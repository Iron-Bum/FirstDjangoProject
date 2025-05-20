from django.urls import path
from example2 import views

urlpatterns = [
    path('', views.main_page),
]