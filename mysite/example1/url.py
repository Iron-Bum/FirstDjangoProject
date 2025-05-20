from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.index),
    path('class/', views.Index2.as_view()),
    path('func/<str:name>/', views.test_value),
]