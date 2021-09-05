from django.urls import path
from thaatee_lms.client_views import (LmsCategoryAPIView, LmsCategoryShortAPIView, LmsSubCategoryAPIView, CoursesAPIView, CourseSectionAPIView,
                                      RateCourseAPIView, ProgressHistoryAPIView, LessonAPIView, CourseDetailedInfoAPIView, CoursesShortInfoAPIView, CourseLessonDisplay, KeyHiglightAPIView, CategoryExpert, EnrolledAPIView)

urlpatterns = [
    path('lmscategory', LmsCategoryAPIView.as_view()),
    path('lmscategory/<int:id>/', LmsCategoryAPIView.as_view()),
    path('shortlmscategory', LmsCategoryShortAPIView.as_view()),
    path('lmssubcategory', LmsSubCategoryAPIView.as_view()),
    path('lmssubcategory/<int:id>/', LmsSubCategoryAPIView.as_view()),
    path('courses', CoursesAPIView.as_view()),
    path('courses/<int:id>/', CoursesAPIView.as_view()),
    path('ratecourse', RateCourseAPIView.as_view()),
    path('ratecourse/<int:id>/', RateCourseAPIView.as_view()),
    path('progresshistory', ProgressHistoryAPIView.as_view()),
    path('progresshistory/<int:id>/', ProgressHistoryAPIView.as_view()),
    path('lesson', LessonAPIView.as_view()),
    path('lesson/<int:id>/', LessonAPIView.as_view()),
    path('coursesection/', CourseSectionAPIView.as_view()),
    path('coursesection/<int:id>/', CourseSectionAPIView.as_view()),
    path('courseDetailed/', CourseDetailedInfoAPIView.as_view()),
    path('courseDetailed/<int:id>/', CourseDetailedInfoAPIView.as_view()),
    path('courseshort/', CoursesShortInfoAPIView.as_view()),
    path('courseshort/<int:id>/', CoursesShortInfoAPIView.as_view()),
    path('courselessondisplay', CourseLessonDisplay.as_view()),
    path('keyhiglight', KeyHiglightAPIView.as_view()),
    path('categoryexpert', CategoryExpert.as_view()),
    path('enrolled', EnrolledAPIView.as_view()),
]
