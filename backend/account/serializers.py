from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, validators=[validate_password])
    # confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model=CustomUser
        fields=['id','first_name','last_name','email','phone','is_active','subcrip','subcrip_type','stripe_checkout_session_id']
        # extra_kwargs = {'password':{'write_only':True}}


    def validate(self,data):
        if CustomUser.objects.filter(email=data).exists():
            raise serializers.ValidationError("This email is already exsist")
        return data
    

    def validate(self,data):
        if CustomUser.objects.filter(phone=data).exists():
            raise serializers.ValidationError("This phone number is already exsist")
        return data        

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
        user = CustomUser.objects.create(email=validated_data['email'])
        user.first_name=validated_data['first_name']
        user.last_name=validated_data['last_name']
        user.phone=validated_data['phone']
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"