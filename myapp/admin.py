from django.contrib import admin
from .models import Invoice, InvoiceDetail

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
  list_display = ['invoice_no', 'date', 'customer_name', 'id']

@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
  list_display = ['invoice', 'description', 'quantity', 'unit_price', 'price', 'id']

