# Generated by Django 3.2.11 on 2022-01-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('apps', '0006_auto_20220107_1814'), ('apps', '0007_auto_20220115_2117'), ('apps', '0008_alter_responsestub_format')]

    dependencies = [
        ('apps', '0005_alter_requestlog_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcestub',
            name='method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE')], default='GET', max_length=10, verbose_name='HTTP Method'),
        ),
        migrations.RenameField(
            model_name='requestlog',
            old_name='body',
            new_name='request_body',
        ),
        migrations.AlterField(
            model_name='requestlog',
            name='request_body',
            field=models.TextField(blank=True, null=True, verbose_name='Request Body'),
        ),
        migrations.RenameField(
            model_name='requestlog',
            old_name='headers',
            new_name='request_headers',
        ),
        migrations.AddField(
            model_name='requestlog',
            name='response_body',
            field=models.TextField(blank=True, null=True, verbose_name='Request Body'),
        ),
        migrations.AddField(
            model_name='requestlog',
            name='response_headers',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Headers'),
        ),
        migrations.AddField(
            model_name='responsestub',
            name='format',
            field=models.CharField(choices=[('JSON', 'JSON'), ('XML', 'XML'), ('PLAIN_TEXT', 'Plain Text')], default='PLAIN_TEXT', max_length=10, verbose_name='Format'),
        ),
    ]
