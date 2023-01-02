from rest_framework import serializers
from .models import empclass
class empserializer(serializers.ModelSerializer):
            class Meta: 
                    model=empclass
                    fields='__all__'
    
     