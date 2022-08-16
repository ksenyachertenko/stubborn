# Generated by Django 3.2.13 on 2022-06-09 13:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0021_auto_20220605_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestStub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('headers', models.JSONField(blank=True, default=dict, verbose_name='Headers')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Response Body')),
                ('description', models.CharField(blank=True, max_length=30, null=True, verbose_name='Short Description')),
                ('format', models.CharField(choices=[('JSON', 'JSON'), ('XML', 'XML'), ('PLAIN_TEXT', 'Text')], default='PLAIN_TEXT', max_length=10, verbose_name='Format')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('uri', models.URLField(verbose_name='URI')),
                ('query_params', models.JSONField(blank=True, default=dict, verbose_name='Query Params')),
                ('method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE'), ('HEAD', 'HEAD'), ('OPTIONS', 'OPTIONS')], default='GET', max_length=10, verbose_name='HTTP Method')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='apps.application')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'request',
                'verbose_name_plural': 'requests',
            },
        ),
        migrations.RemoveField(
            model_name='responsestub',
            name='timeout',
        ),
        migrations.CreateModel(
            name='ResourceHook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('lifecycle', models.CharField(choices=[('before', 'Before request processed'), ('after_req', 'After request processed'), ('after_resp', 'After response returned')], default='after_req', max_length=10)),
                ('action', models.CharField(choices=[('wait', 'Wait'), ('webhook', 'Webhook')], default='wait', max_length=10)),
                ('timeout', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Response Timeout')),
                ('order', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Order')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.requeststub')),
                ('resource', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.resourcestub')),
            ],
            options={
                'verbose_name': 'hook',
                'verbose_name_plural': 'hooks',
                'ordering': ('order',),
            },
        ),
        migrations.AddConstraint(
            model_name='resourcehook',
            constraint=models.UniqueConstraint(fields=('order', 'lifecycle', 'resource'), name='unique_order_per_resource'),
        ),
    ]