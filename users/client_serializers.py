from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from users.models import Role, User, Profile


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')


class UserRenderSerilaizer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=True)

    class Meta:
        model = User
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name',
                  'last_name', 'contact', 'facebook', 'linkdin', 'about', 'youtube', 'website_url', 'education', 'expertise_in', 'profile')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()], 'password': {'write_only': True}
            }
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # user.profile.set(profile_data)
        return user

    def update(self, instance, validated_data):

        profile_data = validated_data.pop('profile')
        if hasattr(validated_data, 'password'):
            instance.set_password(validated_data['password'])

        instance.first_name = validated_data.get(
            'first_name', instance.first_name)

        instance.last_name = validated_data.get(
            'last_name', instance.last_name)

        instance.email = validated_data.get(
            'email', instance.email)

        instance.facebook = validated_data.get(
            'facebook', instance.facebook)

        instance.linkdin = validated_data.get(
            'linkdin', instance.linkdin)

        instance.about = validated_data.get(
            'about', instance.about)

        instance.website_url = validated_data.get(
            'website_url', instance.website_url)

        instance.education = validated_data.get(
            'education', instance.education)

        instance.expertise_in = validated_data.get(
            'expertise_in', instance.expertise_in)

        instance.save()
        instance.profile.set(profile_data)
        return instance
