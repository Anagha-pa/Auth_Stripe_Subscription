from django.urls import path
from .views import Register,PasswordCreation,LoginAPI,UserDetails

urlpatterns = [
    
    path('register/',Register.as_view()),
    path('password-create/',PasswordCreation.as_view()),
    path('login/',LoginAPI.as_view()),
    path('user-details/',UserDetails.as_view()),
    
    
]
