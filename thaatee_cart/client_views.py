from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from thaatee_cart.client_serializers import *
from thaatee_cart.models import *
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status

# Create your views here.


class PromocodeAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin):
    # permission_classes = [permissions.AllowAny]
    serializer_class = PromocodeSerializer
    queryset = Promocode.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['promocode_type']
    search_fields = ['promocode_name']
    ordering_fields = ['promocode_quantity']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class CartAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['courses', 'user']
    # search_fields = ['subcategory_name']
    ordering_fields = ['quantity']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        cart = Cart.objects.filter(
            user=request.data['user'], product_variant=request.data['product_variant'])
        if len(cart) > 0:
            serializer = CartCreateSerializer(
                cart[0], data=request.data, partial=True)
        else:
            serializer = CartCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        cart = Cart.objects.get(pk=id)
        serializer = CartCreateSerializer(
            cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        return self.destroy(request, id)


class CartCheckAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = CartCreateSerializer
    queryset = Cart.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'product_variant', 'user']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        cart = Cart.objects.filter(
            user=request.data['user'], product_variant=request.data['product_variant'])
        if len(cart) > 0:
            serializer = CartCreateSerializer(
                cart[0], data=request.data, partial=True)
        else:
            serializer = CartCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        cart = Cart.objects.get(pk=id)
        serializer = CartCreateSerializer(
            cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        return self.destroy(request, id)


class OrderAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['amount', 'order_id', 'user']
    search_fields = ['order_id']
    ordering_fields = ['amount']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class PaymentList(APIView):

    def get(self, request, format=None):
        data = settings.RAZORPAY_CLIENT.payment.all()

        return Response(data)


class Payment(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        order = settings.RAZORPAY_CLIENT.order.create(data=request.data)
        return Response(order)


class PaymentCapture(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        order = settings.RAZORPAY_CLIENT.order.create(data=request.data)
        return Response(order)
