from rest_framework import serializers

from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, validated_data) -> UserModel:
        user = UserModel.objects.create_user(**validated_data)
        return user
