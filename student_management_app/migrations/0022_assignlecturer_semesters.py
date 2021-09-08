# Generated by Django 3.1.7 on 2021-09-08 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0021_merge_20210908_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('semester_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssignLecturer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('assign_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.courses')),
                ('assign_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.departments')),
                ('assign_intake', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.intakes')),
                ('assign_semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.semesters')),
                ('assign_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('assign_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.subjects')),
            ],
        ),
    ]
