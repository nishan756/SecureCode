from .models import SecureCode, SecureCodeUserPermission, SecureCodeEmailPermission

from rest_framework import serializers



class SecureCodeUserPermissionSerializer(serializers.ModelSerializer):

    class Meta:

        model = SecureCodeUserPermission

        fields = ["secure_code", "user"]
    


class SecureCodeEmailPermissionSerializer(serializers.ModelSerializer):

    class Meta:

        model = SecureCodeEmailPermission

        fields = ["secure_code", "email"]


class SecureCodeSerializer(serializers.ModelSerializer):

    class Meta:

        model = SecureCode

        fields = ["original_url", "code", "expires_at", "created_at", "visibility", "is_valid"]

        read_only_fields = ["created_at", "is_valid"]


class OriginalURLSerializer(serializers.Serializer):

    original_url = serializers.URLField(read_only = True)