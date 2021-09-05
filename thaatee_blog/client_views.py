from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics, mixins,  filters, permissions, status
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from thaatee_blog.client_serializers import RateSerializer, BlogSerializer, SubCategorySerializer, CategorySerializer, EventsSerializer, UpcomingEventsSerializer
from thaatee_blog.models import Rate, Blog, SubCategory, Category, Events
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from datetime import date


class CategoryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_name']
    search_fields = ['category_name']
    ordering_fields = ['category_name']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class SubCategoryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['subcategory_name']
    search_fields = ['subcategory_name']
    ordering_fields = ['subcategory_name']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class BlogAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = BlogSerializer
    pagination_class = LimitOffsetPagination
    LimitOffsetPagination.default_limit = 12
    queryset = Blog.objects.filter(status=True)
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'id', 'slug',
                        'category', 'subcategory', 'popular']
    search_fields = ['user']
    ordering_fields = ['user']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class RateAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user']
    search_fields = ['user']
    ordering_fields = ['user']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class EventsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventsSerializer
    pagination_class = LimitOffsetPagination
    LimitOffsetPagination.default_limit = 12
    queryset = Events.objects.filter(status=True)
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['event_title', 'event_date', 'slug']
    search_fields = ['event_title']
    ordering_fields = ['event_title']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class UpcomingEventsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = UpcomingEventsSerializer
    # pagination_class = LimitOffsetPagination
    # LimitOffsetPagination.default_limit = 12
    queryset = Events.objects.filter(
        event_date__gte=date.today(), status=True).order_by('event_date')
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)
