# Generated by Django 3.0.6 on 2020-05-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200507_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.CharField(default='', max_length=30),
        ),
    ]
