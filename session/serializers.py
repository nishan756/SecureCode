from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()


class UserSignupSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(
        style = {"type":"password"},

        write_only = True
    )

    password = serializers.CharField(
        style = {"type":"password"},

        write_only = True
    )

    class Meta:

        model = User

        fields = ["username", "first_name", "last_name", "email", "image", "is_premium_user", "password", "confirm_password"]

        read_only_fields = ["password"]


    def validate(self, validated_data):

        confirm_password = validated_data.pop("confirm_password", None)

        password = validated_data.get("password", None)

        if not confirm_password:

            raise serializers.ValidationError("You must fill up password confirmation field")

        if not password:

            raise serializers.ValidationError("You must provide password")

        if confirm_password != password:

            raise serializers.ValidationError("Password didn't matched")

        validated_data.pop("confirm_password", None)

        return validated_data

    def create(self, validated_data):

        password = validated_data.pop("password")

        user = User.objects.create(**validated_data)

        user.set_password(password)

        user.save(update_fields = ["password"])

        return user


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["first_name", "last_name", "image"]


class UserPasswordUpdateSerializer(serializers.Serializer):

    old_password = serializers.CharField(
        style = {"type":"password"},
        write_only = True,
    )

    new_password = serializers.CharField(
        style = {"type":"password"},
        write_only = True,
    )

    confirm_password = serializers.CharField(
        style = {"type":"password"},
        write_only = True,
    )


    def validate(self, validated_data):

        old_password = validated_data.get("old_password", None)

        new_password = validated_data.get("new_password", None)

        confirm_password = validated_data.pop("confirm_password", None)

        if not old_password:

            raise serializers.ValidationError("You must provide your old password")

        if not new_password:

            raise serializers.ValidationError("You must provide a new password")

        if not confirm_password:

            raise serializers.ValidationError("Please, confirm your new password")

        if new_password != confirm_password:

            raise serializers.ValidationError("Password didn't match")

        return validated_data


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(

        style = {"input_type":"password",}
        
    )

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username", "id"]

        read_only_fields = ["username", "id"]