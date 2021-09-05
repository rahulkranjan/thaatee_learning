from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from users.models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer()
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name',
                  'last_name', 'contact', 'password')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()], 'password': {'write_only': True}
            }
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        role = Role.objects.get(id=5)
        user_data['roles'] = role
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # if hasattr('validated_data', 'password'):
        # if instance.check_password(validated_data['password']) == False:
        #     instance.set_password(validated_data.get(
        #         'password', instance.password))

        instance.first_name = validated_data.get(
            'first_name', instance.first_name)

        instance.last_name = validated_data.get(
            'last_name', instance.last_name)

        # instance.email = validated_data.get(
        #     'email', instance.email)
        instance.save()
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'contact', 'password', 'first_name',
                  'last_name', 'roles', 'avtar', 'email')
        extra_kwargs = {'password': {'write_only': True}}
