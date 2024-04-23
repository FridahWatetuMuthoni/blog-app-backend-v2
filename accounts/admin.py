from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import CharField, Textarea, TextInput
from django import forms
from django.db import models

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email','username', 'first_name',)
    list_filter = ('email','username', 'first_name', 'is_active', 'is_staff',)
    ordering = ('-start_date',)
    list_display = ('id','email','username', 'first_name','last_name', 'is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields':('email','username', 'first_name',)}),
        ('Permissions',{'fields':('is_active', 'is_staff',)}),
        ('Personal',{'fields':('about','profile_image')})
    )
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':60})}
    }
    
    add_fieldsets = (
        (None, {
            'classes':("wide",),
            'fields':('email','username','first_name','last_name','password1','password2','is_active','is_staff',)
            }),
        )
    
admin.site.register(CustomUser, UserAdminConfig)