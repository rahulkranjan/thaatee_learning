from django.urls import path
from .views import(LmsCategoryAPIView, LmsSubCategoryAPIView, QuizAPIView, QuestionsAPIView,
                   CoursesAPIView, CourseSectionAPIView, RateCourseAPIView, ProgressHistoryAPIView, LessonAPIView, KeyHiglightAPIView, EnrolledAPIView)

urlpatterns = [
    path('lmscategory', LmsCategoryAPIView.as_view()),
    path('lmscategory/<int:id>/', LmsCategoryAPIView.as_view()),
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
    path('quiz', QuizAPIView.as_view()),
    path('quiz/<int:id>/', QuizAPIView.as_view()),
    path('question', QuestionsAPIView.as_view()),
    path('question/<int:id>/', QuestionsAPIView.as_view()),
    path('coursesection/', CourseSectionAPIView.as_view()),
    path('coursesection/<int:id>/', CourseSectionAPIView.as_view()),
    path('keyhighlights/', KeyHiglightAPIView.as_view()),
    path('keyhighlights/<int:id>/', KeyHiglightAPIView.as_view()),
    path('enrolled/', EnrolledAPIView.as_view()),
    path('enrolled/<int:id>/', EnrolledAPIView.as_view()),

]
