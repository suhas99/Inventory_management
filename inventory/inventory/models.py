from django.db import models
import uuid
from django.conf import settings
from rest_framework import generics


class ManagerModel(models.Model):
    Manager = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                               default=True)
    approve=models.BooleanField(default=False)

    class Meta:
        abstract = True


class products(ManagerModel):
    pid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    productName = models.CharField(max_length=25, blank=False, null=False)
    productPrice = models.FloatField(blank=False, null=False)


class vendor(ManagerModel):
    vid = models.IntegerField(primary_key=True)
    vendorName = models.CharField(max_length=25, blank=False, null=False)


class stock(ManagerModel):
    sid = models.ForeignKey(products, on_delete=models.CASCADE,null=False)
    svid = models.ForeignKey(vendor, on_delete=models.CASCADE,null=False)
    batchNum = models.IntegerField(null=False,default=0)
    batchDate = models.DateField(blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)

    class Meta:
        unique_together = (("sid", "svid"),)

    def __str__(self):
        return str(self.sid)

