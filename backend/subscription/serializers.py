from rest_framework.serializers import ModelSerializer
from .models import * 
from account.serializers import RegisterSerializer


class SubscriptionTypeSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields="__all__"



class DashboardSerializer(ModelSerializer):
    user = RegisterSerializer()
    sub_type = SubscriptionTypeSerializer()

    class Meta:
        model = Subscription
        fields = "__all__"

