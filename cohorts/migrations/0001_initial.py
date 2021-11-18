# Generated by Django 3.2.9 on 2021-11-18 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('priest', models.EmailField(max_length=254)),
                ('priestess', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Native',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('native_id', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=225)),
                ('phone_number', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohorts.cohort')),
            ],
        ),
    ]
