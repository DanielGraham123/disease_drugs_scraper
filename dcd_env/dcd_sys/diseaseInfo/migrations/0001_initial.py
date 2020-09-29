# Generated by Django 3.0.4 on 2020-09-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=500)),
                ('description', models.TextField(blank=True, default='', max_length=500000)),
                ('symptoms', models.TextField(blank=True, default='', max_length=5000)),
                ('causes', models.TextField(blank=True, default='', max_length=5000)),
                ('complications', models.TextField(blank=True, default='', max_length=5000)),
                ('risks', models.TextField(blank=True, default='', max_length=5000)),
                ('preventions', models.TextField(blank=True, default='', max_length=5000)),
                ('link', models.URLField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=500)),
                ('generic_name', models.CharField(editable=False, max_length=500)),
                ('other_name', models.CharField(editable=False, max_length=500)),
                ('description', models.TextField(blank=True, default='', max_length=500000)),
                ('uses', models.TextField(blank=True, default='', max_length=5000)),
                ('side_effects', models.TextField(blank=True, default='', max_length=5000)),
                ('precautions', models.TextField(blank=True, default='', max_length=5000)),
                ('interactions', models.TextField(blank=True, default='', max_length=5000)),
                ('storage', models.TextField(blank=True, default='', max_length=5000)),
                ('link', models.URLField(default='', null=True)),
            ],
        ),
    ]
