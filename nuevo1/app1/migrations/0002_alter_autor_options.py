# Generated by Django 4.2.6 on 2023-11-01 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Autores'},
        ),
    ]
