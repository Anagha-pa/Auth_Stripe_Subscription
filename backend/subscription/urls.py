from django.urls import path
from .views import SubscriptionView,UserDashboard

urlpatterns = [
    
    path('subscriptions/',SubscriptionView.as_view()),
    path('user-dashboard/<int:id>/',UserDashboard.as_view()),
    
    
]
