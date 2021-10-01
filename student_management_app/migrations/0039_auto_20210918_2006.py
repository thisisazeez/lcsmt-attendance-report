# Generated by Django 3.2.6 on 2021-09-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0038_students_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='subject',
        ),
        migrations.AddField(
            model_name='attendance',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='media/attendance'),
        ),
    ]
