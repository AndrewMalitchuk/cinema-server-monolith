# Generated by Django 3.0.2 on 2020-01-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_app', '0007_ticket_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='code',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Код'),
        ),
    ]