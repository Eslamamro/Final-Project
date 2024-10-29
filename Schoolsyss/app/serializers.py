from rest_framework import serializers
from .models import Teacher, Student
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'email',
                  ]

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
                raise serializers.ValidationError("This username is already taken.")

        if len(value) < 3:
                raise serializers.ValidationError("Username must be at least 3 characters long.")
        if not value.isalnum():
                raise serializers.ValidationError("Username can only contain letters and numbers.")

        return value




class TeacherSerializer(serializers.ModelSerializer):

    class Meta:

        model = Teacher
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'phoneNumber',
            'address',
            'subject',
            'students'
        ]

    def validate_age(self, value):
        if value < 23 or not value.isdigit():
            raise serializers.ValidationError("Age must be between 3 and 20.")
        return value

    def validate_phoneNumber(self, value):
        if not value.isdigit() or len(value) == 11:
            raise serializers.ValidationError("Enter a valid phone number.")
        return value


class UpdateTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        read_only_fields = ['first_name', 'last_name', 'subject']
        fields = [
            'phoneNumber',
            'address',
        ]

        fields += read_only_fields

    def validate_phoneNumber(self, value):
        if not value.isdigit() or len(value) == 11:
            raise serializers.ValidationError("Enter a valid phone number.")
        return value




class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'parent_phoneNumber',
            'address',
            'student_class',

        ]

    def validate_age(self, value):
        if value < 6 or value > 19 or not value.isdigit():
            raise serializers.ValidationError("Age must be between 6 and 19.")
        return value

    def validate_parent_phoneNumber(self, value):
        if not value.isdigit() or len(value) == 11:
            raise serializers.ValidationError("Enter a valid parent phone number.")
        return value



class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        read_only_fields = ['first_name', 'last_name']
        fields = [
            'user',
            'parent_phoneNumber',
            'address',
        ]

        fields += read_only_fields

    def validate_parent_phoneNumber(self, value):
        if not value.isdigit() or len(value) == 11:
            raise serializers.ValidationError("Enter a valid parent phone number.")
        return value
