# Generated by Django 4.1.7 on 2023-04-17 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_mentee',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_mentor',
        ),
    ]
