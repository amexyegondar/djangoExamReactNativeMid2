from django.shortcuts import render


from django.shortcuts import render
from .models import teclass
from rest_framework import generics
from .serializers import teserializer
class telist(generics.ListCreateAPIView):
                   queryset=teclass.objects.all()
                   serializer_class=teserializer
class tedel(generics.RetrieveUpdateDestroyAPIView):
                   queryset=teclass.objects.all()
                   serializer_class=teserializer
