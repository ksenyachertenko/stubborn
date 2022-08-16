# Generated by Django 3.2.13 on 2022-06-05 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_auto_20220603_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcestub',
            name='tail',
            field=models.CharField(blank=True, default='', max_length=120, verbose_name='URL Tail'),
        ),
        migrations.AlterUniqueTogether(
            name='resourcestub',
            unique_together={('slug', 'method', 'tail')},
        ),
    ]