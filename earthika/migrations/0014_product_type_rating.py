# Generated by Django 3.1.5 on 2021-01-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthika', '0013_auto_20210119_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_type',
            name='rating',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]