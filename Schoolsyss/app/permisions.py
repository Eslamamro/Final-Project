from rest_framework import permissions
from .models import Teacher, Student
from django.contrib import messages


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        teacher = Teacher.objects.get(user=user)
        if teacher.age == '40':
            return False
        else:
            return True


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        student = Student.objects.get(user=user)
        if student.age < '10':
            return False
        else:
            return True
