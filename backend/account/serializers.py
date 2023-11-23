from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model=CustomUser
        fields='__all__'

    def validate(self, data):
        
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError("Password doesn't match")
        

        if 'first_name' in data:
            for i in data['first_name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'name cannot contain numbers'})
                
        if 'last_name' in data:
            for i in data['last_name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'name cannot contain numbers'})
                

        if 'phone' in data :
            num=str(data['phone'])
            if len(num)>10 or len(num)<10:
                raise serializers.ValidationError({'error':'invalid phone number'})
        return data
    

    def create(self, validated_data):
        user = CustomUser.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            )
        return user


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['email','password']