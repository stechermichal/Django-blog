# Generated by Django 2.2.5 on 2019-09-11 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auto',
            new_name='author',
        ),
    ]
