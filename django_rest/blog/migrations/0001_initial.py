# Generated by Django 2.0.7 on 2018-07-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
