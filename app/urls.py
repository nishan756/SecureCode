from .views import get_code, create_code, delete_code, home, my_codes, delete_multiple_code, add_user_permission, add_email_permission, delete_user_permission, delete_email_permission

from django.urls import path


urlpatterns = [
    path("", home, name = "home"),

    path("get/<str:code>/", get_code, name = "get-code"),

    path("my-codes/", my_codes, name = "my-codes"),

    path("create/", create_code, name = "create-code"),

    path("delete/<uuid:id>/", delete_code, name = "delete-code"),

    path("delete-multiple/", delete_multiple_code, name = "delete-multiple-code"),

    path("add-user-permission/<uuid:id>", add_user_permission, name = "add-user-permission"),

    path("add-email-permission/<uuid:id>/", add_email_permission, name = "add-email-permission"),

    path("delete-user-permission/<uuid:id>/", delete_user_permission, name = "delete-user-permission"),

    path("delete-email-permission/<uuid:id>/", delete_email_permission, name = "delete-email-permission"),
]