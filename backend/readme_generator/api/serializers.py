from rest_framework import serializers
from .models import READMERequest

class ReadmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = READMERequest
        fields = ['id', 'url', 'created_at']