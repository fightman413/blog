# Generated by Django 3.0.4 on 2020-04-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogIndex', '0006_auto_20200330_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='articledetail',
            name='IsDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='commentdetail',
            name='IsDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
