from django.db import models
from choices import *

class Product(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True,default='')
    image = models.ImageField(default='', upload_to='media/product', blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.name)

class Product_Type(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,blank=True, related_name='product_name')
    product_type = models.CharField(max_length=100, null=True,blank=True,default='')
    description = models.TextField(max_length=1000,null=True,blank=True,default='')
    image = models.ImageField(default='',upload_to='media/product_type',blank=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True,null=True)
    # price = models.PositiveIntegerField(blank=True,null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.product_type)
class Product_Type_Package(models.Model):
    product_package = models.ForeignKey(Product_Type, on_delete=models.CASCADE, null=True,blank=True, related_name='product_package')
    package_image = models.ImageField(default='',upload_to='media/product_type',blank=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    unit = models.CharField(max_length=20,default='', blank=True)

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

class Enquiry(models.Model):
    first_name = models.CharField(max_length=100, null=True,blank=True,default='')
    last_name = models.CharField(max_length=100, null=True,blank=True,default='')
    email = models.CharField(max_length=100, null=True,blank=True,default='')
    mobile = models.CharField(max_length=100, null=True,blank=True,default='')
    message = models.CharField(max_length=100, null=True,blank=True,default='')
    product = models.ForeignKey(Product_Type, on_delete=models.CASCADE, null=True,blank=True, related_name='enquiry_product')
    status = models.IntegerField(CHOICE_ENQUIRY_STATUS,default=1)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.first_name+' '+self.last_name)