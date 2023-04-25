# Generated by Django 4.1.7 on 2023-04-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_is_admin_alter_customuser_is_mentee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('mentor', 'Mentor'), ('mentee', 'Mentee')], max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_mentee',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_mentor',
            field=models.BooleanField(default=False),
        ),
    ]