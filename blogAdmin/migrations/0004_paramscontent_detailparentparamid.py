# Generated by Django 3.0.3 on 2020-03-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAdmin', '0003_auto_20200315_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='paramscontent',
            name='detailParentParamID',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
