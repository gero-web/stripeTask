# Generated by Django 4.1.7 on 2023-02-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeItem', '0005_alter_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ManyToManyField(to='storeItem.item')),
            ],
        ),
    ]
