# Generated by Django 2.1.7 on 2019-05-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='volunteers',
            field=models.ManyToManyField(to='volunteers.Volunteer'),
        ),
    ]
