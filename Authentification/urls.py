from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *
urlpatterns = [
    # auth/
    # login & logout
    path('login/', MyTokenObtainPairView.as_view(), ),
    path('token/refresh/', TokenRefreshView.as_view(),),
    path('sign_up/',create_User),
    path('logout/',logout),
    # Verification Code
    path('sendCode/',sendVerificationCode),
    path('verifyCode/',verifyVerificationCode),
    # Reset Password
    path('reset_password/',resetPassword),
]