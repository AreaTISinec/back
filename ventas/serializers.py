from rest_framework import serializers
from .models import Ventas

class ventasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ventas
        fields='__all__'