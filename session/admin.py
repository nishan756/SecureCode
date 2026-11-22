from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ["username", "first_name", "last_name", "email", "is_premium_user"]

    list_filter = ["is_premium_user"]

    list_per_page = 500