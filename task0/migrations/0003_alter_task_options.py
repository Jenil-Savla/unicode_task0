# Generated by Django 3.2.5 on 2021-09-07 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task0', '0002_alter_task_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['due']},
        ),
    ]
