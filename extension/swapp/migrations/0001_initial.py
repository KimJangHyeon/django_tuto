# Generated by Django 2.1.3 on 2018-11-30 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('context', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_zone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 12, 1, 0, 53, 10, 431542))),
                ('title', models.CharField(max_length=128)),
                ('context', models.TextField(null=True)),
            ],
        ),
    ]
