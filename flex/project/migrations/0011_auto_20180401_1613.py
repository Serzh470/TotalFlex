# Generated by Django 2.0.3 on 2018-04-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20180401_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='predecessors',
            field=models.ManyToManyField(blank=True, related_name='_task_predecessors_+', to='project.Task'),
        ),
    ]
