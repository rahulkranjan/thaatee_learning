from django.urls import path
from .client_views import *
from django.conf.urls import include, url

urlpatterns = [
    path('pages', PagesAPIView.as_view()),
    path('pages/<int:id>/', PagesAPIView.as_view()),
    path('imggallery', ImgGalleryAPIView.as_view()),
    path('imggallery/<int:id>/', ImgGalleryAPIView.as_view()),
    path('homeslide', HomeSlideAPIView.as_view()),
    path('homeslide/<int:id>/', HomeSlideAPIView.as_view()),
    path('offerslide', OfferSlideAPIView.as_view()),
    path('offerslide/<int:id>/', OfferSlideAPIView.as_view()),
    path('testimonials', TestimonialsAPIView.as_view()),
    path('testimonials/<int:id>/', TestimonialsAPIView.as_view()),
    path('contact', ContactAPIView.as_view()),
    path('contact/<int:id>/', ContactAPIView.as_view()),
    path('faq', FaqAPIView.as_view()),
    path('subscribe', SubscribeAPIView.as_view()),
    path('faq/<int:id>/', FaqAPIView.as_view()),
    path('contactinstructor', ContactInstructorAPIView.as_view()),

]
