from django.urls import path
from example2 import views

urlpatterns = [
    path('', views.main_page),
    path('card/', views.card),
    path('market/', views.market),
]