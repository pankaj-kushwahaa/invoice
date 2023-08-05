from rest_framework import serializers
from .models import Invoice, InvoiceDetail
from pprint import pprint

class InvoiceDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = InvoiceDetail
    fields = ['invoice','description', 'quantity', 'unit_price', 'price']


class InvoiceSerializer(serializers.ModelSerializer):
  details = InvoiceDetailSerializer(many=True, required=False, read_only=True)

  class Meta:
    model = Invoice
    fields = ['id', 'date', 'invoice_no', 'customer_name', 'details']