# Generated by Django 2.0.3 on 2018-03-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20180315_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('project_role', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=250)),
                ('other', models.CharField(max_length=250)),
            ],
        ),
    ]