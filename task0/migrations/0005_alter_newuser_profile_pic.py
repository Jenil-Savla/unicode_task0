# Generated by Django 3.2.5 on 2021-09-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task0', '0004_newuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
