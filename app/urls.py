from .views import get_code, create_code, delete_code, home, my_codes

from django.urls import path


urlpatterns = [
    path("", home, name = "home"),

    path("get/<str:code>/", get_code, name = "get-code"),

    path("my-codes/", my_codes, name = "my-codes"),

    path("create/", create_code, name = "create-code"),

    path("delete/<uuid:id>/", delete_code, name = "delete-code"),
]