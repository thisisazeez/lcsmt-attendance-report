# Generated by Django 3.1.7 on 2021-09-06 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0018_remove_subjects_department_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='department_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.departments'),
        ),
    ]
