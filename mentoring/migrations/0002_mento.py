# Generated by Django 4.1.7 on 2023-03-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=100)),
            ],
        ),
    ]
