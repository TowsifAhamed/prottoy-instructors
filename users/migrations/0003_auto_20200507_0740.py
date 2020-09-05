# Generated by Django 3.0.6 on 2020-05-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Teacher', 'TEACHER'), ('Representative', 'REPRESENTATIVE'), ('Student', 'STUDENT')], default='student', max_length=20),
        ),
    ]
