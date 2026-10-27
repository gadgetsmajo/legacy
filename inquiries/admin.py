from django.contrib import admin

from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('kind', 'name', 'email', 'status', 'created_at')
    list_filter = ('kind', 'status', 'created_at')
    search_fields = ('name', 'email', 'business_name', 'product', 'subject', 'message')
