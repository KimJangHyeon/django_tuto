# Generated by Django 2.1 on 2018-09-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenApp', '0006_auto_20180903_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='uid',
        ),
        migrations.AddField(
            model_name='myuser',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
