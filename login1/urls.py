from django.urls import path
from login1 import views
# from .views import signuppage, loginpage, homepage

urlpatterns = [
    path('signup/', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('home/', views.homepage, name='home'),
    path('logout/', views.Logout, name='logout'),
]