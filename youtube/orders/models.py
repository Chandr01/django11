from django.db import models
from products.models import Product


# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Статус {}'.format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    total_price = models.DecimalField(max_digits=100, decimal_places=1,default=0)
    # цена всех продутков в заказе
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_phone = models.CharField(max_length=48, blank=True, null=True)
    customr_address = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(max_length=500, blank=True, null=True )
    status = models.ForeignKey(Status, default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=100, decimal_places=1, default=0)
    total_price = models.DecimalField(max_digits=100, decimal_places=1, default=0)
    # цена всех похожиш продутков одного типа
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Товар {}'.format(self.product.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
