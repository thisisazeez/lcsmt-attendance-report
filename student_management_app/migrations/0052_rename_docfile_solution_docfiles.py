# Generated by Django 3.2.9 on 2021-11-11 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0051_auto_20211111_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='docfile',
            new_name='docfiles',
        ),
    ]