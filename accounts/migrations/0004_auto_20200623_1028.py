# Generated by Django 3.0.7 on 2020-06-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200623_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/avatars/anonymous.png', upload_to='media/avatars'),
        ),
    ]
