# Generated by Django 3.1.5 on 2021-07-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20210725_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(default='#', max_length=50),
        ),
    ]