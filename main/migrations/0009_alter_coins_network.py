# Generated by Django 3.2.6 on 2021-08-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_coins_network'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='network',
            field=models.CharField(choices=[('BSC', 'Binance Smart Chain'), ('ERC-20', 'Ethereum Network'), ('POLYGON', 'Polygon Network'), ('TRC-20', 'Tron Smart Chain'), ('OEC-20', 'OkEx network'), ('FRC-20', 'Fantom smart chain')], default='BSC', max_length=7),
        ),
    ]
