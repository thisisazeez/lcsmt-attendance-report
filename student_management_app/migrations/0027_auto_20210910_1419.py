# Generated by Django 3.1.7 on 2021-09-10 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0026_auto_20210910_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='department',
            new_name='department_name',
        ),
    ]
