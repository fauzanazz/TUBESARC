from django.urls import path
from FE1 import views
 
urlpatterns = [
    path('signup/', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('', views.homepage, name='home'),
    path('logout/', views.Logout, name='logout'),
    path('YourFess/', views.YourFess, name='yourfess'),
]