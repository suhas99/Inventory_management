from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from .seralizer import productsSerializer
from .models import products, vendor, stock
from django.contrib.auth.models import User
from .seralizer import UserSerializer,vendorSerializer,stockSerializer
from .permission import IsManager
import json


#
# def home(request):
#     response=requests.get('http://127.0.0.1:8000/api/products/?format=json')
#     productsData=response.json()
#     return render(request,'test.html', {
#         'productsData': productsData })


class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]


def product_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = products.objects.all()
        serializer = productsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return render(request, 'test.html', {'productsData':snippets})


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = productsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet since we require id for delete and post and also get using particular id.
    """
    try:
        snippet = products.objects.get(pk=pk)
    except products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = productsSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = productsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def vendor_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = vendor.objects.all()
        serializer = vendorSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return render(request, 'test.html', {'productsData':snippets})


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = vendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail(request, pk):
    """
    Retrieve, update or delete a code snippet since we require id for delete and post and also get using particular id.
    """
    try:
        snippet = vendor.objects.get(pk=pk)
    except vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = vendorSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = vendorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def stock_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = stock.objects.all()
        serializer = stockSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return render(request, 'test.html', {'productsData':snippets})


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = stockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def stock_detail(request, pk):
    """
    Retrieve, update or delete a code snippet since we require id for delete and post and also get using particular id.
    """
    try:
        snippet = stock.objects.get(pk=pk)
    except stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = stockSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = stockSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
