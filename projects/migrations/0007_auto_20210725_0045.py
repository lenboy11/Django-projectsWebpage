# Generated by Django 3.1.5 on 2021-07-24 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210724_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='date_posted',
            new_name='date_created',
        ),
    ]