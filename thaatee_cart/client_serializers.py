from rest_framework import serializers
from thaatee_cart.models import *
from thaatee_lms.client_serializers import CourseShortInfoSerializer


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    courses = CourseShortInfoSerializer()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'courses', 'quantity')


class CartCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
