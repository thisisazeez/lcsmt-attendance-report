# Generated by Django 3.2.9 on 2021-11-14 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0058_remove_docs_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.students'),
        ),
    ]
