# Generated by Django 4.2.9 on 2024-02-24 02:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicationID', models.IntegerField()),
                ('netID', models.CharField(max_length=16)),
                ('scholarshipID', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('essay', models.TextField()),
                ('transcript', models.TextField()),
                ('recommendationLetter', models.TextField()),
                ('status', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarshipID', models.IntegerField()),
                ('applications', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ('awardedApplications', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ('awardAmount', models.IntegerField()),
                ('sponsorID', models.CharField(max_length=255)),
                ('numberAvailable', models.IntegerField()),
                ('majors', models.TextField()),
                ('minors', models.TextField()),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=2)),
                ('deadline', models.DateTimeField()),
                ('otherRequirements', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.IntegerField()),
                ('netID', models.CharField(max_length=16)),
                ('pronouns', models.CharField(max_length=9)),
                ('ethnicity', models.CharField(max_length=100)),
                ('currentYear', models.CharField(max_length=9)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=2)),
                ('majors', models.CharField(max_length=110)),
                ('minors', models.CharField(max_length=110)),
                ('personalStatement', models.TextField()),
                ('workExperience', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField()),
                ('netID', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=24)),
                ('sec1Q', models.CharField(max_length=36)),
                ('sec1A', models.CharField(max_length=64)),
                ('sec2Q', models.CharField(max_length=44)),
                ('sec2A', models.CharField(max_length=64)),
                ('firstName', models.CharField(max_length=35)),
                ('lastName', models.CharField(max_length=35)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('listColumn', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, size=None)),
            ],
        ),
    ]