from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet, home

router = DefaultRouter()
router.register(r'invoice', InvoiceViewSet)
router.register(r'detail', InvoiceDetailViewSet)

urlpatterns = [
  path('', home, name='home'),
  path('api/', include(router.urls)),
]