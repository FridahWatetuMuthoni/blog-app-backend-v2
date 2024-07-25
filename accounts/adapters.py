# adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        email = user.email

        try:
            existing_user = User.objects.get(email=email)
            sociallogin.state['process'] = 'connect'
            sociallogin.connect(request, existing_user)

            # Generate JWT tokens
            refresh = RefreshToken.for_user(existing_user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            print(tokens)
            return tokens

        except User.DoesNotExist:
            print('user does not exist')
            user.save()
            return None
