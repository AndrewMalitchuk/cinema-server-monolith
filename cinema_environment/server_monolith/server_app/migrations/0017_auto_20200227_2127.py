# Generated by Django 3.0.2 on 2020-02-27 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0016_ticket_timeline_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='cinema_id',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='film_id',
        ),
    ]
