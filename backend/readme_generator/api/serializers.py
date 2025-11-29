from rest_framework import serializers

class ReadmeSerializer(serializers.Serializer):
    zip_file = serializers.FileField()