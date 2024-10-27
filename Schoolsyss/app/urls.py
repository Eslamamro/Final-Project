from django.urls import path
from .views import StudentsList, TeachesList, TeacherDetails, StudentDetails
urlpatterns = [
    path('students/', StudentsList.as_view(), name='get-create-students'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='student-details'),
    path('teachers/', TeachesList.as_view(), name='get-create-teachers'),
    path('teachers/<int:pk>/', TeacherDetails.as_view(), name='teacher-details'),
]