# Generated by Django 3.1.7 on 2021-09-11 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0028_auto_20210910_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='course',
        ),
    ]
