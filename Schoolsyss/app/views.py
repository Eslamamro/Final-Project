from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TeacherSerializer, UpdateTeacherSerializer, StudentSerializer, UpdateStudentSerializer
from rest_framework.authtoken.models import Token
from . models import Teacher, Student
from rest_framework import status
# from .permisions import IsTeacher
# Create your views here.


class StudentsList(APIView):

    # permission_classes = [IsTeacher]

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

    # permission_classes = [IsTeacher]

    def get(self, request, pk):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = Student.objects.get(id=pk)
        serializer = UpdateStudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        student = Student.objects.get(id=pk)
        serializer = UpdateStudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)


class TeachesList(APIView):

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
    def get(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = UpdateTeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = UpdateTeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = UpdateTeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Updated Successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        teacher.delete()
        return Response({'message': 'User Deleted Successfully'}, status=status.HTTP_200_OK)


# class Login(APIView):
#
#     def post(self, request):
#         data = request.data
#         print("******************", data)
#         auth = authenticate(**data)
#         user = [Teacher, Student]
#         if user:
#             token, created = Token.objects.get_or_create(user=auth)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)