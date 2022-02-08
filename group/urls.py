from django.urls import path, include
from group import views 

urlpatterns = [
    path('index/', views.index),
    path('contactUs/', views.contactUs),
    path('aboutus/', views.aboutus),
    
]