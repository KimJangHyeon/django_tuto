# Generated by Django 2.1 on 2018-09-03 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokenApp', '0003_auto_20180903_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='id',
            new_name='name',
        ),
    ]
