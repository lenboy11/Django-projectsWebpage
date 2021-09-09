# Generated by Django 3.1.5 on 2021-08-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210724_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.URLField(default='#'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(default='#'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedIn',
            field=models.URLField(default='#'),
        ),
        migrations.AddField(
            model_name='profile',
            name='spotify',
            field=models.URLField(default='#'),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube',
            field=models.URLField(default='#'),
        ),
    ]