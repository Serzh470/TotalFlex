# Generated by Django 2.0.3 on 2018-03-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_merge_20180324_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='successor',
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'Task'), (2, 'Milestone')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Не начато'), (2, 'В работе'), (3, 'Отстает'), (4, 'Выполнено'), (5, 'Приостановлено')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Не начато'), (2, 'В работе'), (3, 'Отстает'), (4, 'Выполнено'), (5, 'Приостановлено')]),
        ),
    ]
