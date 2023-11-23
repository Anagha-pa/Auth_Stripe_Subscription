from django.shortcuts import render
from rest_framework.views import APIView
from .models import SubscriptionType,Subscription
from account.models import CustomUser
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import DashboardSerializer




# Create your views here.


import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class SubscriptionView(APIView):
    def post(self,request):
        data = request.data
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        phone = data['phone']
        sub_type = data['sub_type']

        subscription_type = SubscriptionType.objects.get(type=sub_type)
        user = CustomUser.objects.create(username=email,first_name=first_name,last_name=last_name,email=email,phone=phone)
        subscription = Subscription.objects.create(user=user, subscription_name=subscription_type)

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[{
                    'price_data': {
                        'currency': 'INR',  
                        'product_data': {
                            'name':subscription_type.type ,
                            'images':subscription_type.image
                        },
                        'unit_amount':int(subscription_type.price),
                    },
                    'quantity': 1
                }],
                mode='payment',
                success_url=f'http://localhost:3000/Register/subId={subscription.id}',
                cancel_url=f'http://localhost:3000/Register/'
            )
            return Response(data=checkout_session.url)
        except Exception as e:
            print(e)
            return Response(
                data={'message': 'Oops!Some error occured!'},
                status=status.HTTP_400_BAD_REQUEST
            )




class UserDashboard(generics.RetrieveAPIView):
    serializer_class = DashboardSerializer
    queryset=Subscription.objects.all()
    lookup_field="id"
        

        

