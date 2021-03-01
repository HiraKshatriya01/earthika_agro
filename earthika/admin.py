from django.contrib import admin

from earthika.models import *
from django.utils.html import format_html

# Register your models here.


class EnquiryAdmin(admin.ModelAdmin):
    model = Enquiry
    list_display = ['first_name', 'message', 'mobile', 'product']
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Product)

class Product_Type_PackageInline(admin.TabularInline):
    model = Product_Type_Package
    extra = 2

    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 130px; \
                           height: 100px"/>'.format(obj.img))

class Product_Type_Admin(admin.ModelAdmin):
    inlines = [Product_Type_PackageInline]
    list_display = ('product_type','product',  'active')
    # list_display = ('product', 'product_type', 'price', 'created', 'modified', 'active')
    # search_fields = ('product_name','product_type','date_created','date_updated',)

admin.site.register(Product_Type, Product_Type_Admin)
