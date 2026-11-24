from django.db import models

from django.conf import settings

from django.core.exceptions import ValidationError

import uuid


class SecureCode(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "secure_codes")

    original_url = models.URLField()

    code = models.CharField(max_length = 6, unique = True)

    class Visibility(models.TextChoices):

        PUBLIC = "public", "Public"

        PRIVATE = "private", "Private"


    visibility = models.CharField(max_length = 8, default = Visibility.PUBLIC, choices = Visibility.choices)

    expires_at = models.DateTimeField(blank = True, null = True)

    is_valid = models.BooleanField(default = True)

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return self.code

    class Meta:

        ordering = ["is_valid", "-created_at"]


class SecureCodeUserPermission(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    secure_code = models.ForeignKey(SecureCode, on_delete = models.CASCADE, related_name = "user_code_permissions")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):

        return f"{self.user.username} -> {self.secure_code}"

    def clean(self, *args, **kwargs):

        if self.user == self.secure_code.user:

            raise ValidationError("OOPS! You cant assign userself as permitted user. You're already the owner of the secure code")

    class Meta:

        unique_together = ["secure_code", "user"]

        indexes = [
            models.Index(fields = ["user"]),
            models.Index(fields = ["secure_code", "user"])
        ]


class SecureCodeEmailPermission(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    secure_code = models.ForeignKey(SecureCode, on_delete = models.CASCADE, related_name = "email_code_permissions")

    email = models.EmailField()

    def __str__(self):

        return self.email

    class Meta:

        ordering = ["email",]

        indexes = [
            models.Index(fields = ["email",]),
            models.Index(fields = ["secure_code", "email"]),
        ]

        unique_together = ["secure_code", "email"]