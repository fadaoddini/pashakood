from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pashakood.settings import MEDIA_URL, MEDIA_ROOT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('info/', include('info.urls')),
    path('login/', include('custom_login.urls')),
    path('chat/', include('chat.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
