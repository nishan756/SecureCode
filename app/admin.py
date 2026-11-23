from django.contrib import admin

from .models import SecureCode, SecureCodeUserPermission, SecureCodeEmailPermission


@admin.register(SecureCode)
class SecureCodeAdmin(admin.ModelAdmin):

    list_display = ["user", "code", "is_valid"]

    list_per_page = 500

    list_filter = ["is_valid"]

    actions = ["mark_selected_secure_code_as_invalid", "mark_selected_secure_code_as_valid"]

    def mark_selected_secure_code_as_invalid(self, request, queryset):

        count = queryset.update(is_valid = False)

        return self.message_user(request, f"Successfully marked ({count}) secure code as invalid")

    def mark_selected_secure_code_as_valid(self, request, queryset):
    
        count = queryset.update(is_valid = True)
    
        return self.message_user(request, f"Successfully marked ({count}) secure code as valid")
    