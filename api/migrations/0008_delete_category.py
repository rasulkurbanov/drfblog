# Generated by Django 4.1.1 on 2022-09-08 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
