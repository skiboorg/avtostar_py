# Generated by Django 2.1.5 on 2019-01-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20190120_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Ссылка'),
        ),
    ]