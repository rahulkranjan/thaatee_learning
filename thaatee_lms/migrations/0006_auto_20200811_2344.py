# Generated by Django 3.0.7 on 2020-08-11 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thaatee_lms', '0005_auto_20200811_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.TextField(blank=True, null=True)),
                ('no_of_option', models.IntegerField(blank=True, null=True)),
                ('hint', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='level_type',
            field=models.CharField(choices=[('beginner', 'BEGINNER'), ('advanced', 'ADVANCED'), ('intermidate', 'INTERMIDATE')], default='beginner', max_length=20),
        ),
        migrations.AddField(
            model_name='courses',
            name='seo_description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='seo_keyword',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='seo_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='shot_description',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='lesson',
            name='upload_Video',
            field=models.ImageField(blank=True, null=True, upload_to='video/'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.TextField(blank=True, null=True)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('passing_percentage', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('course_section', models.ForeignKey(blank=True, limit_choices_to={'status': True}, null=True, on_delete=django.db.models.deletion.PROTECT, to='thaatee_lms.CourseSection')),
            ],
            options={
                'db_table': 'quiz',
            },
        ),
    ]
