# Generated by Django 2.1 on 2018-10-13 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='slug',
            new_name='slug1',
        ),
    ]
