from django.urls import path
from thaatee_cart.views import *

urlpatterns = [
    path('promocode', PromocodeAPIView.as_view()),
    path('promocode/<int:id>/', PromocodeAPIView.as_view()),
    path('cart', CartAPIView.as_view()),
    path('cart/<int:id>/', CartAPIView.as_view()),
    path('order', OrderAPIView.as_view()),
    path('order/<int:id>/', OrderAPIView.as_view()),


]
