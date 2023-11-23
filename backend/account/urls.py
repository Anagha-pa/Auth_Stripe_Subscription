from django.urls import path
from .views import Register,GoogleLoginView

urlpatterns = [
    
    path('register/',Register.as_view()),
    path('google-login/',GoogleLoginView.as_view()),
    
]
