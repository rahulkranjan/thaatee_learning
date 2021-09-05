from django.urls import path
from thaatee_cart.client_views import *

urlpatterns = [
    path('promocode', PromocodeAPIView.as_view()),
    path('promocode/<int:id>/', PromocodeAPIView.as_view()),
    path('cart', CartAPIView.as_view()),
    path('cart/<int:id>/', CartAPIView.as_view()),
    path('checkcart', CartCheckAPIView.as_view()),
    path('order', OrderAPIView.as_view()),
    path('order/<int:id>/', OrderAPIView.as_view()),
    path('payment', Payment.as_view()),

]
