# Generated by Django 3.1.5 on 2021-01-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthika', '0010_auto_20210119_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_type',
            name='package_image1_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image2_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image3_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image4_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image5_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
