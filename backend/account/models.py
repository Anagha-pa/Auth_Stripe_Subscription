from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from subscription.models import SubscriptionType

class CustomUserManager(BaseUserManager):
    
    def _create_user(self, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone, password, **extra_fields)

    def create_superuser(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=100, unique=True,null=True,blank=True)
    phone = models.IntegerField(unique=True,null=True,blank=True) 
    is_active = models.BooleanField(default=False,null=True,blank=True)
    subcrip = models.BooleanField(default=False,null=True,blank=True)
    subcrip_type = models.ForeignKey(SubscriptionType,on_delete=models.CASCADE)
    stripe_checkout_session_id = models.IntegerField(unique=True,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']

    objects = CustomUserManager()

    groups = models.ManyToManyField("auth.Group", related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField("auth.Permission", related_name="custom_user_permissions", blank=True)
