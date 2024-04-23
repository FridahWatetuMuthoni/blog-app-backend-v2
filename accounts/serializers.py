from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(RegisterSerializer):
    about = serializers.CharField(max_length=250, required=False)
    profile_image = serializers.ImageField(required=False)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    
    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        print(cleaned_data)
        cleaned_data['first_name'] = self.validated_data.get('first_name', '')
        cleaned_data['last_name'] = self.validated_data.get('last_name','')
        cleaned_data['about'] = self.validated_data.get('about','')
        if(self.validated_data.get('profile_image')):
            cleaned_data['profile_image'] = self.validated_data.get('profile_image','')
        print(cleaned_data)
        return cleaned_data
    
    def save(self, request):
        user = super(UserRegistrationSerializer,self).save(request)
        user.first_name = self.cleaned_data.get('first_name','')
        user.last_name = self.cleaned_data.get('last_name','')
        user.about = self.cleaned_data.get('about', '')
        user.profile_image = self.cleaned_data.get('profile', None)
        user.save()
        return user
    
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','about','profile_image']
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','username','first_name','last_name','about','profile_image','last_login']
        read_only_fields = ['last_login']
