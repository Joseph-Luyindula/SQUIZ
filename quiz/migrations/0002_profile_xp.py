# Generated by Django 5.1.4 on 2025-06-10 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
