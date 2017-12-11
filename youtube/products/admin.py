from django.contrib import admin
from .models import Product, ProductImage


#
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    # list_filter = ['name']
    # search_fields = ['name', 'email']
    class Meta:
        model = Product


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    # list_filter = ['name']
    # search_fields = ['name', 'email']
    class Meta:
        model = ProductImage


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImagesAdmin)
