# Generated by Django 3.1.5 on 2021-01-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthika', '0009_auto_20210119_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_type',
            name='package_image1_price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image2_price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image3_price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image4_price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='package_image5_price',
            field=models.IntegerField(default=1),
        ),
    ]
