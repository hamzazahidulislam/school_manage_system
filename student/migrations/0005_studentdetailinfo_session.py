# Generated by Django 3.0.6 on 2020-05-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200521_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetailinfo',
            name='session',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
