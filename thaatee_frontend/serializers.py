from rest_framework import serializers
from thaatee_frontend.models import Pages, HomeSlide, OfferSlide, ImgGallery, Testimonials, Contact, Faq, ContactInstructor, Subscribe


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'


class ImgGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgGallery
        fields = '__all__'


class HomeSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSlide
        fields = '__all__'


class OfferSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferSlide
        fields = '__all__'


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class ContactInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInstructor
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
