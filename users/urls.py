from django.urls import path
from .views import authenticate_user, UserRetrieveUpdateAPIView, RoleAPIView, UserAPIView, Current_User


urlpatterns = [
    path('auth', authenticate_user),
    path('current_user/', Current_User),
    path('role/', RoleAPIView.as_view()),
    path('role/<id>/', RoleAPIView.as_view()),
    path('userm/', UserAPIView.as_view()),
    path('userm/<id>/', UserAPIView.as_view()),

]
