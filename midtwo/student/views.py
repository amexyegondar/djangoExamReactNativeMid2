from django.shortcuts import render


from django.shortcuts import render
from .models import stuclass
from rest_framework import generics
from .serializers import stuserializer
class stulist(generics.ListCreateAPIView):
                   queryset=stuclass.objects.all()
                   serializer_class=stuserializer
class studel(generics.RetrieveUpdateDestroyAPIView):
                   queryset=stuclass.objects.all()
                   serializer_class=stuserializer