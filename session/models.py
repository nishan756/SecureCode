from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    image = models.ImageField(upload_to = "user_image/", blank = True, null = True)

    is_premium_user = models.BooleanField(default = False)

    email = models.EmailField(unique = True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username",]