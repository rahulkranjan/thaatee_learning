# Generated by Django 3.0.8 on 2020-09-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thaatee_frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'subscribe',
            },
        ),
    ]
