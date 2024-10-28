from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default="Unknown")
    last_name = models.CharField(max_length=50, default="Unknown")
    age = models.CharField(max_length=2)
    phoneNumber = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=50)
    Subject_choices = (
        ('Math', 'Math'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
        ('Geography', 'Geography'),
        ('History', 'History'),
        ('Arabic', 'Arabic'),
        ('English', 'English'),
        ('French', 'French'),
    )
    subject = models.CharField(choices=Subject_choices, max_length=50)
    students = models.ManyToManyField('Student', blank=True, related_name='teachers')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Teacher'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default="Unknown")
    last_name = models.CharField(max_length=50, default="Unknown")
    age = models.CharField(max_length=2)
    parent_phoneNumber = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=50)
    student_class = models.CharField(max_length=4)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Student'


class Course(models.Model):
    pass
