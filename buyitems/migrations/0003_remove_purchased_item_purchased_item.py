# Generated by Django 4.2 on 2023-04-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyitems', '0002_item_purchased_purchased'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchased',
            name='item',
        ),
        migrations.AddField(
            model_name='purchased',
            name='item',
            field=models.ManyToManyField(related_name='purchased_Item', to='buyitems.item_purchased'),
        ),
    ]
