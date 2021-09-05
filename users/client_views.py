from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework import mixins
from .client_serializers import RoleSerializer, UserSerializer, ProfileSerializer, UserRenderSerilaizer
from .models import Role,  User, Profile
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters, status


class ProfileAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'id'
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['name']
    # search_fields = ['name']
    # ordering_fields = ['name']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class RoleAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class UserAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['email', 'first_name',
                        'last_name', 'roles', 'id', 'contact', 'profile']
    search_fields = ['email']
    ordering_fields = ['first_name']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)


class UserRenderAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRenderSerilaizer
    pagination_class = LimitOffsetPagination
    LimitOffsetPagination.default_limit = 12
    queryset = User.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['email', 'first_name',
                        'last_name', 'roles', 'id', 'contact', 'profile', 'visible_home']
    search_fields = ['email']
    ordering_fields = ['first_name']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)
