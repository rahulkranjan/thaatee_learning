from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from thaatee_frontend.serializers import PagesSerializer, HomeSlideSerializer, OfferSlideSerializer, ImgGallerySerializer, TestimonialsSerializer, ContactsSerializer, FaqSerializer, ContactInstructorSerializer, SubscribeSerializer
from thaatee_frontend.models import Pages, HomeSlide, OfferSlide, ImgGallery, Testimonials, Contact, Faq, ContactInstructor, Subscribe
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PagesAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = PagesSerializer
    queryset = Pages.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'created_at', 'status', 'slug']
    search_fields = ['name']
    ordering_fields = ['name']

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


class ImgGalleryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = ImgGallerySerializer
    queryset = ImgGallery.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'status']
    search_fields = ['name']
    ordering_fields = ['name']

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


class HomeSlideAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = HomeSlideSerializer
    queryset = HomeSlide.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'created_at', 'status']
    search_fields = ['name']
    ordering_fields = ['name', 'position']

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


class OfferSlideAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = OfferSlideSerializer
    pagination_class = SmallPagination
    queryset = OfferSlide.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'created_at', 'status']
    search_fields = ['name']
    ordering_fields = ['name', 'position']

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


class TestimonialsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = TestimonialsSerializer
    pagination_class = SmallPagination
    queryset = Testimonials.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'status']
    search_fields = ['name']
    ordering_fields = ['name']

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


class TestimonialsAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = TestimonialsSerializer
    pagination_class = SmallPagination
    queryset = Testimonials.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'status']
    search_fields = ['name']
    ordering_fields = ['name']

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


class ContactAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = ContactsSerializer
    pagination_class = SmallPagination
    queryset = Contact.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'status']
    search_fields = ['name']
    ordering_fields = ['name']

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


class FaqAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = FaqSerializer
    pagination_class = SmallPagination
    queryset = Faq.objects.all()
    lookup_field = 'id'

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


class ContactInstructorAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                               mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                               mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = ContactInstructorSerializer
    pagination_class = SmallPagination
    queryset = ContactInstructor.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'status']
    search_fields = ['name']
    ordering_fields = ['name']

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


class SubscribeAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = SubscribeSerializer
    pagination_class = SmallPagination
    queryset = Subscribe.objects.all()
    lookup_field = 'id'

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
