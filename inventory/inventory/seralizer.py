from rest_framework import serializers
from . import models
from rest_framework import routers


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class productsSerializer(serializers.ModelSerializer):
    manager = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.products
        fields = ('pid', 'productName', 'productPrice')


class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.vendor
        fields = ('vid', 'vendorName')


class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.stock
        fields = ('sid', 'svid', 'batchNum', 'batchDate', 'quantity')
