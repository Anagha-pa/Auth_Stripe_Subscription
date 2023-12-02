from django.urls import path
from .views import StripePayment

urlpatterns = [
    
    path('stripe-payment/<int:id>',StripePayment.as_view()),
    
    
    
]
