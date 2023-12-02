from django.shortcuts import render
from rest_framework.views import APIView
from .models import SubscriptionType
from account.models import CustomUser
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import SubscriptionTypeSerializer




# Create your views here.


import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY



class StripePayment(APIView):
    def post(self,request):
   
            try:
                subscriptiontype = SubscriptionType.objects.get(id=request.data.get('subscriptiontype'))
                checkout_session = stripe.checkout.Session.create(
                    line_items=[{
                        'price_data': {
                            'currency': 'INR',  
                            'product_data': {
                                'name':subscriptiontype.type ,
                                'images':subscriptiontype.image
                            },
                            'unit_amount':int(subscriptiontype.price),
                        },
                        'quantity': 1
                    }],
                    metadata={
                        "subcrip_type_id":subscriptiontype.id
                    },
                    mode='payment',
                    success_url=f'http://localhost:3000/Register/subId={subscriptiontype.id}',
                    cancel_url=f'http://localhost:3000/Register/'
                )
                user_data=CustomUser.objects.get(id=request.data.get("user_data_id"))
                user_data.subcrip_type = subscriptiontype.type
                user_data.stripe_checkout_session_id = checkout_session.id
                user_data.subcrip = True
                user_data.save()
                return Response(data={'url': checkout_session.url})
            except Exception as e:
                return Response(data={'message': 'Oops!Some error occured!'},status=status.HTTP_400_BAD_REQUEST)
            

    def get(self,request):
        try:
            subscriptiontypes = SubscriptionType.objects.all()
            serializer = SubscriptionTypeSerializer(subscriptiontypes, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e :
             return Response(data={'message':'Oops!Some error occurred !'},status=status.HTTP_400_BAD_REQUEST)
    
        


        

        






        

        

