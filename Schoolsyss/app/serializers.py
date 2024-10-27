from rest_framework import serializers
from .models import Teacher, Student
from django.contrib.auth.models import User












class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = Teacher
        fields = [
            'username',
            'password',
            'last_name',
            'phoneNumber',
            'address',
            'subject',
        ]


class UpdateTeacherSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    password1 = serializers.CharField(source='user.password1')
    password2 = serializers.CharField(source='user.password2')

    class Meta:
        model = Teacher
        read_only_fields = ['first_name', 'last_name', 'subject']
        fields = [
            'username',
            'password1',
            'password2',
            'phoneNumber',
            'address',
        ]

        fields += read_only_fields


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password1 = serializers.CharField(source='user.password1')
    password2 = serializers.CharField(source='user.password2')

    class Meta:
        model = Student
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'parent_phoneNumber',
            'address',

        ]


class UpdateStudentSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    password1 = serializers.CharField(source='user.password1')
    password2 = serializers.CharField(source='user.password2')

    class Meta:
        model = Student
        read_only_fields = ['first_name', 'last_name']
        fields = [
            'username',
            'password1',
            'password2',
            'parent_phoneNumber',
            'address',
        ]

        fields += read_only_fields
