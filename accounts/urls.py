from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BlackListRefreshTokenView, GoogleLogin, FacebookLogin,UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/<int:pk>/', UserView.as_view(), name='user_detail'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/',BlackListRefreshTokenView.as_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
]