from rest_framework import serializers
from thaatee_frontend.models import Pages, HomeSlide, OfferSlide, ImgGallery, Testimonials, Contact, Faq,  Subscribe, ContactInstructor


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ('id', 'name', 'seo_title', 'seo_description',
                  'seo_keyword', 'page_content', 'slug', 'status', 'page_count')


class ImgGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgGallery
        fields = ('id', 'name', 'status', 'product_image')


class HomeSlideSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeSlide
        fields = ('id', 'name', 'position', 'status',
                  'product_image', 'description', 'urls')


class OfferSlideSerializer(serializers.ModelSerializer):

    class Meta:

        model = OfferSlide
        fields = ('id', 'name', 'position', 'status',
                  'product_image', 'description', 'long_description')


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInstructor
        fields = '__all__'


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
