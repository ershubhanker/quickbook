from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='home'),
    path('hello/', views.my_view, name='hello'),
]
