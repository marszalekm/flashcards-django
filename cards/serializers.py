from rest_framework import serializers
from .models import Word

class WordSerializer(serializers.ModelSerializer):
    # original = serializers.CharField(max_length=50)
    # translation = serializers.CharField(max_length=50)
    class Meta:
        model = Word
        fields = '__all__'