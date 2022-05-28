# Generated by Django 3.2.13 on 2022-05-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('attendence_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField()),
                ('assignee_id', models.IntegerField()),
                ('supervisor_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('is_logged_id', models.BooleanField()),
            ],
        ),
    ]
