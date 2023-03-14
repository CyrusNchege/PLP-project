# Generated by Django 4.1.7 on 2023-03-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=250)),
                ('studentage', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=250)),
                ('studentmajor', models.CharField(default='undeclared', max_length=100)),
                ('campus', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
