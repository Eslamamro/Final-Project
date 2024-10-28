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
from django.contrib import messages
# Create your views here.


class UsersList(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = CreateUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = CreateUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = CreateUserSerializer(user)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = CreateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = CreateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response({'message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)


class StudentsList(APIView):
    permission_classes = [IsAuthenticated, IsTeacher, IsAdminUser]

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetails(APIView):
    permission_classes = [IsAuthenticated, IsStudent, IsAdminUser]

    def get(self, request, pk):
        user_id = request.user.id
        student = Student.objects.get(id=pk)
        if user_id == student.user.id:
            serializer = StudentSerializer(student)
            return Response(serializer.data,  status=status.HTTP_200_OK)
        else:
            return Response({'massage': 'No Do Not Have The Permission TO Access This Page'},
                            status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        user_id = request.user.id
        student = Student.objects.get(id=pk)
        if user_id == student.user.id:
            serializer = UpdateStudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user_id = request.user.id
        student = Student.objects.get(id=pk)
        if user_id == student.user.id:
            serializer = UpdateStudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)


class TeachesList(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        print('***************************', data)
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetails(APIView):
    permission_classes = [IsAuthenticated, IsTeacher, IsAdminUser]

    def get(self, request, pk):
        user_id = request.user.id
        teacher = Teacher.objects.get(id=pk)
        if user_id == teacher.user.id:
            serializer = UpdateTeacherSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'massage': 'No Do Not Have The Permission TO Access This Page'},
                            status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        user_id = request.user.id
        teacher = Teacher.objects.get(id=pk)
        if user_id == teacher.user.id:
            serializer = UpdateTeacherSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user_id = request.user.id
        teacher = Teacher.objects.get(id=pk)
        if user_id == teacher.user.id:
            serializer = UpdateTeacherSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        teacher.delete()
        return Response({'message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)


class Login(APIView):

    def post(self, request):
        data = request.data
        user = authenticate(**data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)