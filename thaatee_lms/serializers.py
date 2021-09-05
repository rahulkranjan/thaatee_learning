from rest_framework import serializers
from thaatee_lms.models import *


class LmsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsCategory
        fields = '__all__'


class LmsSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsSubCategory
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class RateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateCourse
        fields = '__all__'


class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSection
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class ProgressHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressHistory
        fields = '__all__'


class KeyHiglightSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyHiglight
        fields = '__all__'


class EnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolled
        fields = '__all__'
