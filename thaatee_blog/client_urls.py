from django.urls import path
from .client_views import *
from django.conf.urls import include, url

urlpatterns = [
    path('rate', RateAPIView.as_view()),
    path('rate/<int:id>', RateAPIView.as_view()),
    path('blog', BlogAPIView.as_view()),
    path('blog/<int:id>', BlogAPIView.as_view()),
    path('subcategory', SubCategoryAPIView.as_view()),
    path('subcategory/<int:id>', SubCategoryAPIView.as_view()),
    path('category', CategoryAPIView.as_view()),
    path('category/<int:id>', CategoryAPIView.as_view()),
    path('events', EventsAPIView.as_view()),
    path('events/<int:id>/', EventsAPIView.as_view()),
    path('upcomingevents', UpcomingEventsAPIView.as_view()),
    path('upcomingevents/<int:id>/', UpcomingEventsAPIView.as_view()),
]
