# Generated by Django 3.1.5 on 2021-07-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210719_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='frontpic',
            field=models.ImageField(default='default_post.png', upload_to='front_pics'),
        ),
    ]
