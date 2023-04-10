from django.shortcuts import render
from rest_framework import generics, parsers
from .models import Item, Category
from .serializers import CategorySerializer, ItemSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
