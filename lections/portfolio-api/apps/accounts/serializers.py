from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
    ValidationError,
)
from rest_framework.validators import UniqueValidator

User = get_user_model()


class RegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password": "Password didn't match"})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ChangePasswordSerializer(ModelSerializer):
    old_password = CharField(write_only=True, required=True)
    password = CharField(write_only=True, required=True, validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password": "Password didn't match"})
        return super().validate(attrs)

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise ValidationError({"old_password": "Old password do not match"})
        return value

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user.pk != instance.pk:
            raise ValidationError({"authorize": "You don't have permission"})
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class UpdateUserSerializer(ModelSerializer):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )

    def validate_email(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise ValidationError({"email": "This email is already exist"})
        return value

    def validate_username(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise ValidationError({"username": "This username is already exist"})
        return value

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user.pk != instance.pk:
            raise ValidationError({"authorize": "You don't have permission"})
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")

        instance.save()
        return instance
