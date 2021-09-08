# Generated by Django 3.1.7 on 2021-09-04 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0011_courses_department_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.departments'),
        ),
    ]
