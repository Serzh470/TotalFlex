# Generated by Django 2.0.3 on 2018-03-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20180328_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='project_role',
            field=models.SmallIntegerField(choices=[(1, 'Участник'), (2, 'Менеджер'), (3, 'Стейкхолдер')]),
        ),
    ]