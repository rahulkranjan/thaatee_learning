# Generated by Django 3.0.8 on 2020-09-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200926_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ManyToManyField(to='users.Profile'),
        ),
    ]
