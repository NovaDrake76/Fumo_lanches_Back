from django.shortcuts import render
from rest_framework import generics, parsers
from .models import Item
from .serializers import ItemSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
