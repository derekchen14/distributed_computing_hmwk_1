# Generated by Django 2.1.5 on 2019-01-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('STUDENT_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('STUDENT_NAME', models.CharField(max_length=20)),
                ('STDUENT_YEAR', models.CharField(max_length=20)),
                ('REGISTERED_COURSES', models.CharField(max_length=500)),
            ],
        ),
    ]
