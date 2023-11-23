from django.contrib import admin
from .models import SubscriptionType,Subscription

# Register your models here.

admin.site.register(SubscriptionType)
admin.site.register(Subscription)