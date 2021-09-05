from rest_framework import serializers
from thaatee_blog.models import Blog, SubCategory, Category, Rate, Events
from users.models import User


class AuthorSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class BlogSerializer(serializers.ModelSerializer):

    user = AuthorSeralizer()

    class Meta:
        model = Blog
        fields = ('id', 'user', 'blog_title', 'category', 'subcategory',
                  'content', 'viwes_count', 'slug', 'created_at', 'modified_at', 'blog_image', 'popular', 'status')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'subcategory_name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'slug', 'category_name')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'blog', 'user', 'rate', 'comment')


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'user', 'event_title', 'event_image', 'event_description',
                  'small_description', 'event_location', 'event_price', 'event_date', 'event_time', 'status', 'slug')


class UpcomingEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'event_title',
                  'small_description', 'event_location',  'event_date', 'slug')
