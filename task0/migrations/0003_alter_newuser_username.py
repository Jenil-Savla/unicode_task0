# Generated by Django 3.2.5 on 2021-09-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task0', '0002_remove_newuser_native_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
