from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name']
    search_fields = ['name', 'email']


# Register your models here.
admin.site.register(Subscriber, SubscriberAdmin)
