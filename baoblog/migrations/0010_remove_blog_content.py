# Generated by Django 2.0.7 on 2018-07-20 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baoblog', '0009_auto_20180717_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]