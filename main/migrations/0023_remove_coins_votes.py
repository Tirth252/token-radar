# Generated by Django 3.2.6 on 2021-08-20 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210820_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coins',
            name='votes',
        ),
    ]
