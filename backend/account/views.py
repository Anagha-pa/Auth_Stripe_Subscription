from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,UserCreateSerializer
from .models import CustomUser




# Create your views here.
class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'User registered successfully'}, status=status.HTTP_201_CREATED)
            return Response({'message':'User With this email or mobile number already exists',},status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'message': 'An error occurred during registration.'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GoogleLoginView(APIView):
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        

        try:
            user_exists = CustomUser.objects.filter(email=email).exists()

            if user_exists:
                return Response(
                    {"message": "User already exist"}, status=status.HTTP_200_OK
                )

            else:
                data = {
                    "email": email,
                    "password": password,
                   
                }

                serializer = UserCreateSerializer(data=data)
                if serializer.is_valid():
                    user = serializer.save()
                    return Response(
                        {"message": "User created successfully"},
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )

        except Exception as e:
            print(str(e))
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    