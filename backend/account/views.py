from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,UserDetailSerializer
from .models import CustomUser
from django.contrib.auth import authenticate,login
from rest_framework import generics




# Create your views here.
class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                user=serializer.save()
                return Response({'message':'User registered successfully'}, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)
            return Response(data={'message': 'Oops! Some error occurred!'}, status=status.HTTP_400_BAD_REQUEST)
        


class PasswordCreation(APIView):
    def post(self,request):
        user_data = CustomUser.objects.get(id=request.data.get('user_data_id'))
        password = request.data.get('password')
        confrim_password = request.data.get('confrim_password')

        if password != confrim_password:
            return Response({'message':'password and confrim password is not matches'},status=status.HTTP_400_BAD_REQUEST)
        
        user_data.set_password(password)
        user_data.is_active = True
        user_data.save()
        return Response({'message':'Password created successfully'},status=status.HTTP_200_OK)



class LoginAPI(APIView):
        def post(self,request):
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(request, email=email,password=password)
            
            if user:
                login(request,user)
                return Response({'message':'user login successfully'},status=status.HTTP_200_OK)
            return Response({'message':'Invalid Credenitials'},status=status.HTTP_401_UNAUTHORIZED)
            


class UserDetails(generics.RetrieveAPIView):    
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'        