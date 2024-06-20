from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.core.exceptions import PermissionDenied
from .customFilters import *
from django_filters.rest_framework import DjangoFilterBackend

class DeadlineCustomPermission(BasePermission):
     def has_permission(self, request, view):
         return request.user.groups.filter(name='admin').exists()

class DeadlineCustomPermission(BasePermission):
     def has_permission(self, request, view):
         if request.method == 'POST':
             return request.user.has_perm('main.add_invoces')
         if request.method == 'DELETE':
             return request.user.has_perm('main.delete_invoces')
         if request.method == 'PUT':
             return request.user.has_perm('main.change_invoces')                
         return False
class ReadWriteSerializerMixin(object):
    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
            "'%s' should either include a `read_serializer_class` attribute,"
            "or override the `get_read_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` attribute,"
            "or override the `get_write_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.write_serializer_class

class CustomUserView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
class ProductCategoryView(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Product.objects.all()
    write_serializer_class = ProductWriteSerializer
    read_serializer_class = ProductReadSerializer

class InvoiceView(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class  = InvoiceFilter
    ordering_fields = '__all__'

    def get_queryset(self):
        user = self.request.user
        return Invoice.objects.filter(customerCNPJ=user.registrationNumber)

class InvoiceItemView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = InvoiceItem.objects.all()
    write_serializer_class = InvoiceItemWriteSerializer
    read_serializer_class = InvoiceItemReadSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class  = InvoiceItemFilter
    ordering_fields = '__all__'

class WarrantyView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Warranty.objects.all()
    write_serializer_class = WarrantyWriteSerializer
    read_serializer_class = WarrantyReadSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class  = WarrantyFilter
    ordering_fields = '__all__'