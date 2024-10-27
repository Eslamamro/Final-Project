# from rest_framework import permissions
# from .models import Teacher,Student
#
#
# class IsTeacher(permissions.BasePermission):
#     def has_permission(self, request, view):
#         data = request.Teacher
#         teacher = Teacher.objects.get(User=data)
#         if teacher.isTeacher:
#             return True

# class IsStudent(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         student = Student.objects.get(user=user)
#         if student.isStudent:
#             return True
#         else:
#             return False
