# Generated by Django 3.1.5 on 2021-01-21 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earthika', '0016_auto_20210120_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enquiry_product', to='earthika.product_type'),
        ),
    ]
