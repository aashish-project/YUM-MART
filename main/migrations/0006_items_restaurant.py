# Generated by Django 4.2 on 2023-04-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='restaurant',
            field=models.ManyToManyField(related_name='restaurant', to='main.restaurants'),
        ),
    ]
