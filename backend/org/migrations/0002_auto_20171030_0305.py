# Generated by Django 2.0b1 on 2017-10-30 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'Organization', 'verbose_name_plural': 'Organizations'},
        ),
    ]