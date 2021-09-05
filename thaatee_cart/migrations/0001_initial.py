# Generated by Django 3.0.8 on 2020-09-22 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thaatee_lms', '0014_courses_selling_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promocode_name', models.CharField(blank=True, max_length=100)),
                ('promocode_quantity', models.IntegerField(default=0)),
                ('promocode_type', models.CharField(blank=True, choices=[('value', 'VALUE OFF'), ('percentage', 'PERCENTAGE OFF')], default='value', max_length=20, null=True)),
                ('promocode_payment', models.CharField(blank=True, choices=[('online_wallet', 'ONLINE WALLET'), ('card', 'CARD')], default='online', max_length=20, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'promocode',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('amount', models.IntegerField()),
                ('payment', models.TextField(blank=True, default='', null=True)),
                ('promocode_details', models.TextField(blank=True, default='', null=True)),
                ('order_details', models.TextField(blank=True, default='', null=True)),
                ('order_status', models.TextField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')),
                ('payment_status', models.TextField(blank=True, default='', null=True)),
                ('payment_choice', models.CharField(blank=True, choices=[('online_wallet', 'ONLINE WALLET'), ('card', 'CARD')], max_length=20, null=True)),
                ('paytment_details', models.TextField(blank=True, default='', null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('promocode', models.ForeignKey(blank=True, limit_choices_to={'status': True}, null=True, on_delete=django.db.models.deletion.PROTECT, to='thaatee_cart.Promocode')),
                ('user', models.ForeignKey(limit_choices_to={'roles': 3}, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='thaatee_lms.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]