from django.urls import path

from .views import GroupsAPIView

urlpatterns = [
    path('api/v1/', GroupsAPIView.as_view(), name='main'),
]