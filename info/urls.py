from django.urls import path, re_path
from info.views import info, update_info, Profile, update_info_image

urlpatterns = [
    path('before/info/', info, name='info-before'),
    path('update/before/', update_info, name='update-info-before'),
    path('profile/', Profile.as_view(), name='profile'),
    path('update/profile/', update_info, name='update-info-profile'),
    path('update/profile/image/', update_info_image, name='update-info-profile-image'),
]
