# Generated by Django 3.1.5 on 2021-01-18 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthika', '0002_auto_20210118_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_type',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
