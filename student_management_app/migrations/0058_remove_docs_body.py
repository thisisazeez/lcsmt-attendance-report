# Generated by Django 3.2.9 on 2021-11-13 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0057_docs_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docs',
            name='body',
        ),
    ]
