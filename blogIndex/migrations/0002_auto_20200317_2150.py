# Generated by Django 3.0.3 on 2020-03-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogIndex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articledetail',
            old_name='articleTags',
            new_name='articleTagsName',
        ),
        migrations.AddField(
            model_name='articledetail',
            name='articleTagsID',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
