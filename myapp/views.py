from django.shortcuts import render
from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer


def home(request):
  url = request.build_absolute_uri("/")
  return render(request, 'myapp/home.html', dict(url=url))

class InvoiceViewSet(viewsets.ModelViewSet):
  queryset = Invoice.objects.all()
  serializer_class = InvoiceSerializer

class InvoiceDetailViewSet(viewsets.ModelViewSet):
  queryset = InvoiceDetail.objects.all()
  serializer_class = InvoiceDetailSerializer

