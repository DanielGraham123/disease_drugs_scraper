# Generated by Django 3.0.4 on 2022-08-09 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseaseInfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='storage',
            new_name='overdose',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='other_name',
        ),
    ]