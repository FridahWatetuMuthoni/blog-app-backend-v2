from django.utils import timezone
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, email, username, first_name,last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is False:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is False:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        
        return self.create_user(email, username, first_name, last_name, password, **other_fields)
    
    def create_user(self, email, username, first_name,last_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username = username, first_name=first_name, last_name=last_name, **other_fields)
        
        user.set_password(password)
        user.start_date = timezone.now()
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('Email Address'), unique=True)
    username = models.CharField(verbose_name=_('Username'),max_length=150, unique=True)
    first_name = models.CharField(verbose_name=_('First Name'),max_length=150, blank=True)
    last_name = models.CharField(verbose_name=_('Last Name'),max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(verbose_name=_('About'), max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', default='default.jpg', blank=True, null=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
        return self.email 