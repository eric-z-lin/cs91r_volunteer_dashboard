# Generated by Django 2.1.7 on 2019-03-25 20:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('address', models.CharField(max_length=256)),
                ('time', models.DateTimeField(default=datetime.datetime(2019, 4, 1, 20, 20, 40, 768083, tzinfo=utc))),
                ('volunteers', models.ManyToManyField(blank=True, related_name='events_volunteers', to='volunteers.Volunteer')),
            ],
        ),
    ]
