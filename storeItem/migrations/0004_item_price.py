# Generated by Django 4.1.7 on 2023-02-17 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeItem', '0003_remove_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
