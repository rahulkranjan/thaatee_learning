from django.urls import path
from .views import RateAPIView, BlogAPIView, SubCategoryAPIView, CategoryAPIView, EventsAPIView

urlpatterns = [
    path('rate', RateAPIView.as_view()),
    path('rate/<int:id>/', RateAPIView.as_view()),
    path('blog', BlogAPIView.as_view()),
    path('blog/<int:id>/', BlogAPIView.as_view()),
    path('subcategory', SubCategoryAPIView.as_view()),
    path('subcategory/<int:id>/', SubCategoryAPIView.as_view()),
    path('category', CategoryAPIView.as_view()),
    path('category/<int:id>/', CategoryAPIView.as_view()),
    path('events', EventsAPIView.as_view()),
    path('events/<int:id>/', EventsAPIView.as_view()),


]
