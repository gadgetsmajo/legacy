from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name', 'weight', 'unit_price', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('reference', 'customer_name', 'customer_email', 'total', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('reference', 'customer_name', 'customer_email', 'customer_phone')
    readonly_fields = ('reference', 'total', 'created_at', 'updated_at')
    inlines = (OrderItemInline,)
