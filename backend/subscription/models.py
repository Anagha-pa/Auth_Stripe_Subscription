from django.db import models
from account.models import CustomUser



# Create your models here.
class SubscriptionType(models.Model):
    type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='psy_tasks/')
    validity = models.PositiveBigIntegerField(default=30)

    def __str__(self):
        return self.type
    

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    subscription_name = models.ForeignKey(SubscriptionType,on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)


