# Generated by Django 3.2.6 on 2021-09-17 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0034_attendancereport'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='intake',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.intakes'),
        ),
    ]
