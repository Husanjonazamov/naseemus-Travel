from config.env import env
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import exceptions, serializers

OTP_SIZE = env.int("OTP_SIZE", 4)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # attrs contains 'email' instead of 'username' because of USERNAME_FIELD
        data = super().validate(attrs)
        return data

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)

    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise exceptions.ValidationError(_("Email already registered."), code="unique")
        return value

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password"]



class ConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=OTP_SIZE, min_length=OTP_SIZE)
    phone = serializers.CharField(max_length=255)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        user = get_user_model().objects.filter(email=value)
        if user.exists():
            return value

        raise serializers.ValidationError(_("User does not exist"))


class ResetConfirmationSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=OTP_SIZE, max_length=OTP_SIZE)
    email = serializers.EmailField()

    def validate_email(self, value):
        user = get_user_model().objects.filter(email=value)
        if user.exists():
            return value
        raise serializers.ValidationError(_("User does not exist"))



class ResendSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)
