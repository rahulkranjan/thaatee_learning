# Generated by Django 3.0.8 on 2020-10-09 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thaatee_lms', '0017_keyhiglight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyhiglight',
            old_name='document',
            new_name='highlight_img',
        ),
        migrations.RemoveField(
            model_name='keyhiglight',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='keyhiglight',
            name='embedded_link',
        ),
        migrations.RemoveField(
            model_name='keyhiglight',
            name='link',
        ),
        migrations.RemoveField(
            model_name='keyhiglight',
            name='upload_Video',
        ),
        migrations.RemoveField(
            model_name='keyhiglight',
            name='video_link',
        ),
        migrations.RemoveField(
            model_name='keyhiglight',
            name='youtube_link',
        ),
    ]
