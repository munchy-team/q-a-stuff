# Generated by Django 3.2.11 on 2022-02-01 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0026_auto_20220201_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='munchy',
            old_name='data',
            new_name='date',
        ),
    ]
