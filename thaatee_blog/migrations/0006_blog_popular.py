# Generated by Django 3.0.8 on 2020-09-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thaatee_blog', '0005_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]
