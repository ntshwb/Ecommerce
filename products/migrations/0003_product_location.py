# Generated by Django 2.2.3 on 2019-07-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
    ]
