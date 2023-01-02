from django.shortcuts import render
from .models import empclass
from rest_framework import generics
from .serializers import empserializer
class emplist(generics.ListCreateAPIView):
                   queryset=empclass.objects.all()
                   serializer_class=empserializer
class empdel(generics.RetrieveUpdateDestroyAPIView):
                   queryset=empclass.objects.all()
                   serializer_class=empserializer