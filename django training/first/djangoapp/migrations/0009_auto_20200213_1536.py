# Generated by Django 3.0.3 on 2020-02-13 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_remove_userdata_followings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comments',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
