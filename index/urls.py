from django.urls import path, re_path

from index.views import MainIndex

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
]
