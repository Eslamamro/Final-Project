from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TeacherSerializer, UpdateTeacherSerializer, StudentSerializer, UpdateStudentSerializer, CreateUserSerializer
from rest_framework.authtoken.models import Token
from . models import Teacher, Student, User
from rest_framework import status
from .permisions import IsTeacher, IsStudent
from django.core.exceptions import ValidationError, PermissionDenied
from django.contrib import messages
# Create your views here.


class UsersList(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        try:
            users = User.objects.all()
            serializer = CreateUserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to view this resource'},
                            status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            serializer = CreateUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to view this resource'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = CreateUserSerializer(user)
            return Response(serializer.data,  status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to view this resource'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = CreateUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to update this user'},
                            status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = CreateUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to view this resource'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return Response({'message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to view this resource'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentsList(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        try:
            user = request.user
            teacher = Teacher.objects.get(user=user)
            students = teacher.students.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to create a user'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            data = request.data
            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to create a user'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentDetails(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request, pk):
        try:
            user_id = request.user.id
            student = Student.objects.get(id=pk)
            if user_id == student.user.id:
                serializer = StudentSerializer(student)
                return Response(serializer.data,  status=status.HTTP_200_OK)
            else:
                raise PermissionDenied("You do not have permission to view this resource")
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        try:
            user_id = request.user.id
            student = Student.objects.get(id=pk)
            if user_id == student.user.id:
                serializer = UpdateStudentSerializer(student, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied("You do not have permission to view this resource")
        except PermissionDenied:
            return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def patch(self, request, pk):
        try:
            user_id = request.user.id
            student = Student.objects.get(id=pk)
            if user_id == student.user.id:
                serializer = UpdateStudentSerializer(student, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied("You do not have permission to view this resource")
        except PermissionDenied:
            return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return Response({'message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to view this resource'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeachesList(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        try:
            teacher = Teacher.objects.all()
            serializer = TeacherSerializer(teacher, many=True)
            return Response(serializer.data,  status=status.HTTP_200_OK)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to create a user'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            data = request.data
            serializer = TeacherSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to create a user'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeacherDetails(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request, pk):
        try:
            user_id = request.user.id
            print('**************************', user_id)
            teacher = Teacher.objects.get(id=pk)
            if user_id == teacher.user.id:
                serializer = UpdateTeacherSerializer(teacher)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
               raise PermissionDenied("You do not have permission to view this resource")
        except PermissionDenied:
            return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user_id = request.user.id
            teacher = Teacher.objects.get(id=pk)
            if user_id == teacher.user.id:
                serializer = UpdateTeacherSerializer(teacher, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            raise PermissionDenied("You do not have permission to view this resource")
        except PermissionDenied:
            return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self, request, pk):
        try:
            user_id = request.user.id
            teacher = Teacher.objects.get(id=pk)
            if user_id == teacher.user.id:
                serializer = UpdateTeacherSerializer(teacher, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            raise PermissionDenied("You do not have permission to view this resource")
        except PermissionDenied:
            return Response(status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            teacher = Teacher.objects.get(id=pk)
            teacher.delete()
            return Response({'message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to view this resource'}, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Login(APIView):

    def post(self, request):
        data = request.data
        user = authenticate(**data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)