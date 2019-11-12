"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import api_views
from .views import product_detail,product_list,UserDetail,UserList,vendor_detail,vendor_list


# from .api import router
# from .core import views as myapp_views


router = routers.DefaultRouter()
router.register(r'products',api_views.productsViewset)
router.register(r'vendor',api_views.vendorViewset)
router.register(r'stock', api_views.stockViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/',include(router.urls) ),

    # path('a/',home),
    path('product/<str:pk>',product_detail),
    path('products/', product_list),

    path('vendor/<str:pk>', vendor_detail),
    path('vendors/', vendor_list),

    path('vendor/<str:pk>', stock_detail),
    path('vendors/', stock_list),

    path('users',UserList.as_view()),
    path('users/<int:pk>',UserDetail.as_view()),


]
