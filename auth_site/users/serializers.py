from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

# make username optional


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    # validate password when creating a user. You can also use a library for this like django-passwords
    def validate(self, data):
        user = User(**data)
        password = data.get('password')
        try:
            validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            # display list of errors
            raise exceptions.ValidationError(
                {'password': serializer_errors['non_field_errors']})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
