from rest_framework import viewsets
from . import models
from . import seralizer
from .permission import IsManager
from rest_framework import permissions




class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]


class productsViewset(viewsets.ModelViewSet):
    queryset = models.products.objects.all()
    serializer_class = seralizer.productsSerializer
    permission_classes = [IsManager]


class vendorViewset(viewsets.ModelViewSet):
    queryset = models.vendor.objects.all()
    serializer_class = seralizer.vendorSerializer


class stockViewset(viewsets.ModelViewSet):
    queryset = models.stock.objects.all()
    serializer_class = seralizer.stockSerializer



