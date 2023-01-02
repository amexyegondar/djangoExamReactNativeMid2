from rest_framework import serializers
from .models import teclass
class teserializer(serializers.ModelSerializer):
           class Meta:
                    model=teclass
                    fields='__all__'