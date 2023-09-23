from rest_framework import serializers
from api.models import File

class FileFieldFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'