# Generated by Django 5.0 on 2023-12-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
