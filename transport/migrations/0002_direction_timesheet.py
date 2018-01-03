# Generated by Django 2.0b1 on 2018-01-03 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Direction',
                'verbose_name_plural': 'Directions',
            },
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveSmallIntegerField(verbose_name='Version')),
                ('validity', models.DateField(verbose_name='Validity')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_sheets', to='transport.Direction', verbose_name='Direction')),
            ],
            options={
                'verbose_name': 'TimeSheet',
                'verbose_name_plural': 'TimeSheets',
            },
        ),
    ]