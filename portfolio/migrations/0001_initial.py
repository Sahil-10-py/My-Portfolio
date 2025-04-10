# Generated by Django 5.1.6 on 2025-03-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('dob', models.DateField()),
                ('gmail', models.EmailField(max_length=254)),
                ('phone', models.ImageField(upload_to='')),
                ('city', models.CharField(max_length=50)),
                ('projects', models.TextField(max_length=100)),
            ],
        ),
    ]
