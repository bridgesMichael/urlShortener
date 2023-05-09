from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('encode/', views.encodeURL),
    path('decode/', views.decodeURL),
]
