from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    permissions = serializers.JSONField()