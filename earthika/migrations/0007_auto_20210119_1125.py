# Generated by Django 3.1.5 on 2021-01-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthika', '0006_auto_20210119_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_type',
            name='price',
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image5_price',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
