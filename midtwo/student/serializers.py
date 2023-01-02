from rest_framework import serializers
from .models import stuclass
class stuserializer(serializers.ModelSerializer):
                class Meta:
                    model=stuclass
                    fields='__all__'