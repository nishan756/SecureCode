from .models import SecureCode

from rest_framework import serializers

class SecureCodeSerializer(serializers.ModelSerializer):

    class Meta:

        model = SecureCode

        fields = ["original_url", "code", "expires_at", "created_at", "visibility", "is_valid"]

        read_only_fields = ["created_at", "is_valid"]


class OriginalURLSerializer(serializers.Serializer):

    original_url = serializers.URLField(read_only = True)