# Generated by Django 3.2.6 on 2021-09-18 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0037_auto_20210918_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.subjects'),
        ),
    ]