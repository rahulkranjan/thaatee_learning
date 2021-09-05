from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from thaatee_lms.client_serializers import (LmsCategorySerializer, LmsCategoryRenderSerializer, LmsSubCategorySerializer,
                                            CourseSectionSerializer, RateCourseSerializer, LessonSerializer, CoursesSerializer, ProgressHistorySerializer, CourseDetailedInfoSerializer, CourseShortInfoSerializer, KeyHiglightSerializer, EnrolledSerializer)
from .models import LmsCategory, LmsSubCategory, Courses, RateCourse, Lesson, CourseSection, ProgressHistory, KeyHiglight, Enrolled
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status
from django.db.models import Sum, Count, Avg, F, ExpressionWrapper
from django_mysql.models import GroupConcat
from django.conf import settings


class LmsCategoryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = LmsCategorySerializer
    queryset = LmsCategory.objects.filter(status=True)
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_name', 'slug', 'popular', 'display_home']
    search_fields = ['category_name']
    ordering_fields = ['category_name']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class LmsCategoryShortAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = LmsCategoryRenderSerializer
    queryset = LmsCategory.objects.filter(status=True)
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_name', 'slug', 'popular', 'display_home']
    search_fields = ['category_name']
    ordering_fields = ['category_name']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class LmsSubCategoryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = LmsSubCategorySerializer
    queryset = LmsSubCategory.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['subcategory_name']
    search_fields = ['subcategory_name']
    ordering_fields = ['subcategory_name']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class CoursesAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['course_name', 'category', 'status',
                        'subcategory', 'insturctor', 'level_type', 'commission_type', 'slug', 'popular', 'display_home']
    search_fields = ['course_name']
    ordering_fields = ['course_name']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class KeyHiglightAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = KeyHiglightSerializer
    queryset = KeyHiglight.objects.filter(status=True).order_by('position')
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['course', 'course__slug']
    search_fields = ['course']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class RateCourseAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = RateCourseSerializer
    queryset = RateCourse.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user']
    search_fields = ['user']
    ordering_fields = ['user']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

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


class LessonAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['lesson_name', 'course_section']
    search_fields = ['lesson_name']
    ordering_fields = ['lesson_name']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class CourseSectionAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSectionSerializer
    queryset = CourseSection.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['section_name', 'course']
    search_fields = ['section_name']
    ordering_fields = ['section_name']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class ProgressHistoryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                             mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProgressHistorySerializer
    queryset = ProgressHistory.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['course']
    search_fields = ['course']
    ordering_fields = ['course']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class CourseDetailedInfoAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                                mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseDetailedInfoSerializer
    queryset = Lesson.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['lesson_name']
    search_fields = ['section_name']
    ordering_fields = ['section_name']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class CoursesShortInfoAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseShortInfoSerializer
    queryset = Courses.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['course_name', 'status', 'display_home']
    search_fields = ['course_name']
    ordering_fields = ['course_name']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)


class CourseLessonDisplay(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        course = self.request.query_params.get('course', None)
        query = {}

        if course != '' and course is not None:
            query['course_section__course__id'] = course

        if course is not None:
            lesson = Lesson.objects.filter(**query).values('lesson_name', 'lesson_duration', 'content_type',
                                                           'course_section__section_name').order_by('course_section__section_position')
            return Response(lesson)
        else:
            return Response("No data", status=status.HTTP_400_BAD_REQUEST)


class CategoryExpert(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        category = self.request.query_params.get('category', None)
        query = {}

        if category != '' and category is not None:
            query['category'] = category

        if category is not None:
            expert = Courses.objects.filter(**query, popular=True).values('insturctor__id', 'insturctor__first_name', 'insturctor__last_name', 'insturctor__short_info',
                                                                          'insturctor__avtar').annotate(insturctor__profile__profile_name=GroupConcat('insturctor__profile__profile_name', distinct=True)).distinct()[:5]
            return Response(expert)
        else:
            return Response("No data", status=status.HTTP_400_BAD_REQUEST)


class EnrolledAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = EnrolledSerializer
    queryset = Enrolled.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['user', 'course']
    search_fields = ['course']
    ordering_fields = ['course']

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)
