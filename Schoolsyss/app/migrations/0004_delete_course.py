# Generated by Django 5.1.1 on 2024-10-27 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_teacher_students'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]