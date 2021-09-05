from django.urls import path
from .client_views import RoleAPIView, UserAPIView, ProfileAPIView, UserRenderAPIView


urlpatterns = [
    path('role/', RoleAPIView.as_view()),
    path('role/<int:id>/', RoleAPIView.as_view()),
    path('userm/', UserAPIView.as_view()),
    path('userm/<id>/', UserAPIView.as_view()),
    path('profile', ProfileAPIView.as_view()),
    path('homeprofile', UserRenderAPIView.as_view()),

]
