# Generated by Django 2.0.5 on 2018-05-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20180422_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='calculated_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='optimistic_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='pessimistic_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='realistic_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
