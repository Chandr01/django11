from django.contrib import admin
from .models import Order, ProductInOrder, Status


class ProductInOrdersInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrdersInline]

    # list_filter = ['name']
    # search_fields = ['name', 'email']
    class Meta:
        model = Order


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    # list_filter = ['name']
    # search_fields = ['name', 'email']
    class Meta:
        model = ProductInOrder


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(Status, StatusAdmin)
