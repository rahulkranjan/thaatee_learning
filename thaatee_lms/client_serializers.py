from rest_framework import serializers
from thaatee_lms.models import *
from users.client_serializers import UserSerializer
from django.db.models.functions import Coalesce
from django.db.models import Sum, Count, Avg, F, ExpressionWrapper, Q


class LmsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsCategory
        fields = ('id', 'category_name', 'slug', 'status',
                  'origin', 'description', 'facts', 'category_image', 'display_home')


class LmsCategoryRenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsCategory
        fields = ('id', 'category_name', 'slug',
                  'category_image', 'status', 'display_home')


class RateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateCourse
        fields = ('courses', 'user', 'rate', 'id')


class LmsSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsSubCategory
        fields = ('id', 'subcategory_name', 'slug', 'status')


class CoursesSerializer(serializers.ModelSerializer):
    category = LmsCategoryRenderSerializer()
    rate = serializers.SerializerMethodField()
    insturctor = UserSerializer()

    class Meta:
        model = Courses
        fields = ('id', 'course_name', 'slug', 'course_image', 'category',
                  'subcategory', 'requirements', 'description', 'insturctor', 'status', 'rate', 'short_description', 'course_price', 'selling_price', 'display_home', 'popular')

    def get_rate(self, obj):
        data = RateCourse.objects.filter(courses=obj.id).values('courses').annotate(rate_sum=Coalesce(Sum('rate'), 0), total_review=Count('rate'), one_star=Count('rate', filter=Q(rate=1)), two_star=Count('rate', filter=Q(rate=2)), three_star=Count('rate', filter=Q(rate=3)), four_star=Count('rate', filter=Q(
            rate=4)), five_star=Count('rate', filter=Q(rate=5))).annotate(per_one=(F('one_star')/Coalesce(Count('rate'), 1))*100, per_two=(F('two_star')/Coalesce(Count('rate'), 1))*100, per_three=(F('three_star')/Coalesce(Count('rate'), 1))*100, per_four=(F('four_star')/Coalesce(Count('rate'), 1))*100, per_five=(F('five_star')/Coalesce(Count('rate'), 1))*100)
        if data:
            return data[0]
        else:
            data1 = {
                'avg_rate': 0,
                'total_review': 0,
                'one_star': 0,
                'two_star': 0,
                'three_star': 0,
                'four_star': 0,
                'five_star': 0,
                'per_one': 0,
                'per_two': 0,
                'per_three': 0,
                'per_four': 0,
                'per_five': 0,

            }
            return data1


class KeyHiglightSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyHiglight
        fields = ('id', 'course', 'position', 'highlight_img', 'description')


class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSection
        fields = ('id', 'course', 'section_name')


class CourseSectionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseSection
        fields = ('__all__')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lesson
        fields = ('__all__')


class ShowCourseDataSerializer(serializers.ModelSerializer):

    class Meta:

        model = Courses
        fields = ('id', 'course_name')


class ShowCourseSectionDataSerializer(serializers.ModelSerializer):

    class Meta:

        model = CourseSection
        fields = ('id', 'section_name')


class CourseSectionDetailedSerializer(serializers.ModelSerializer):
    course = CoursesSerializer()

    class Meta:

        model = CourseSection
        fields = ('id', 'course', 'section_name', 'status')


class ShowLessonDataSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lesson
        fields = ('id', 'lesson_name', 'created_at')


class ProgressHistorySerializer(serializers.ModelSerializer):

    course = ShowCourseDataSerializer()
    course_section = ShowCourseSectionDataSerializer()
    # lesson = ShowLessonDataSerializer()

    class Meta:
        model = ProgressHistory
        fields = ('__all__')


class ProgressHistoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgressHistory
        fields = ('__all__')


class CourseShortInfoSerializer(serializers.ModelSerializer):
    # category = LmsCategoryRenderSerializer()
    rate = serializers.SerializerMethodField()
    insturctor = UserSerializer()

    class Meta:
        model = Courses
        fields = ('id', 'course_name', 'course_image',
                  'description', 'insturctor', 'rate', 'course_price', 'selling_price', 'display_home', 'short_description')

    def get_rate(self, obj):
        return RateCourse.objects.filter(courses=obj.id).values('courses').annotate(avg_rate=Coalesce(Sum('rate'), 0)/Coalesce(Count('rate'), 1), total_review=Count('rate'))


class CourseDetailedInfoSerializer(serializers.ModelSerializer):
    course_section = CourseSectionDetailedSerializer()

    class Meta:

        model = Lesson
        fields = ('id', 'content_type', 'course_section', 'lesson_name',
                  'lesson_icon', 'description', 'lesson_duration', 'document')


class EnrolledSerializer(serializers.ModelSerializer):
    course = CourseShortInfoSerializer()

    class Meta:

        model = Enrolled
        fields = ('__all__')
