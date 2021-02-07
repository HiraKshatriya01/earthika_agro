# Generated by Django 3.1.5 on 2021-01-18 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earthika', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='enquiry',
            name='status',
            field=models.IntegerField(default=1, verbose_name=((1, 'PENDING'), (2, 'CONTACTED'), (2, 'NO RESPONSE'))),
        ),
        migrations.CreateModel(
            name='Product_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('image', models.ImageField(default='', upload_to='media/product_type')),
                ('package_image1', models.ImageField(default='', upload_to='media/product_type')),
                ('package_image2', models.ImageField(default='', upload_to='media/product_type')),
                ('package_image3', models.ImageField(default='', upload_to='media/product_type')),
                ('package_image4', models.ImageField(default='', upload_to='media/product_type')),
                ('package_image5', models.ImageField(default='', upload_to='media/package_im0age')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_name', to='earthika.product')),
            ],
        ),
    ]