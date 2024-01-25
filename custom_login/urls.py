from django.urls import path, re_path

from custom_login.views import register_user, verify_otp, logouti, VerifyCode, SendOtp

urlpatterns = [
    path('', register_user, name='login-mobile'),
    path('verify/', verify_otp, name='verify-otp'),
    path('logout/', logouti, name='logout'),
    path('sendOtp', SendOtp.as_view(), name='send-otp'),
    path('verifyCode', VerifyCode.as_view(), name='send-otp'),
]
