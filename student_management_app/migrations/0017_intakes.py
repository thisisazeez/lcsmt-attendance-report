# Generated by Django 3.1.7 on 2021-09-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0016_auto_20210904_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intakes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('intake_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]