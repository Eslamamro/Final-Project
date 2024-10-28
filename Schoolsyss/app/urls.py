from django.urls import path
from .views import StudentsList, TeachesList, TeacherDetails, StudentDetails, UsersList, UserDetails, Login
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('users/', UsersList.as_view(), name='get-create-users'),
    path('users/<int:pk>/', UserDetails.as_view(), name='get-create-users'),
    path('students/', StudentsList.as_view(), name='user-details'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='student-details'),
    path('teachers/', TeachesList.as_view(), name='get-create-teachers'),
    path('teachers/<int:pk>/', TeacherDetails.as_view(), name='teacher-details'),
]