from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
from sorl.thumbnail.fields import ImageField


# Create your models here.
class User(AbstractUser):
    avatar = ImageField(null=True, blank=True, upload_to="images/profile_pics/%Y/%m/%d/")
    phone_number = PhoneNumberField(region="UZ", verbose_name=_("phone number"), null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)

        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return tokens
