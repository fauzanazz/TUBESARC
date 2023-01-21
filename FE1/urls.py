from django.urls import path
from FE1 import views

urlpatterns = [
 path('',views.first, name='first'),
 path('profile/',views.profile, name='profile')
]
