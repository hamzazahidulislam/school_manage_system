# Generated by Django 3.0.3 on 2020-06-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=10)),
                ('roll', models.IntegerField()),
                ('gpa', models.IntegerField()),
            ],
        ),
    ]
