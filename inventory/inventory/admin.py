from django.contrib import admin

from .models import products, vendor, stock


class productsAdmin(admin.ModelAdmin):
    list_display = ('pid', 'productName', 'productPrice')


class vendorAdmin(admin.ModelAdmin):
    list_display = ('vid', 'vendorName')


class stockAdmin(admin.ModelAdmin):
    list_display = ('sid', 'svid', 'batchNum', 'batchDate', 'quantity')


admin.site.register(products, productsAdmin)
admin.site.register(vendor, vendorAdmin)
admin.site.register(stock, stockAdmin)
