# Generated by Django 4.1.1 on 2022-09-08 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
