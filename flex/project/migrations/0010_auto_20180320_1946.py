# Generated by Django 2.0.3 on 2018-03-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20180320_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='predecessor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='successor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]