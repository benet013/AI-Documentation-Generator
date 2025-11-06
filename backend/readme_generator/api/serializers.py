from rest_framework import serializers

class ReadmeSerializer(serializers.Serializer):
    # name = serializers.CharField()
    # stack = serializers.CharField()
    zip_file = serializers.FileField()