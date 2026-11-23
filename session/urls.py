from django.urls import path

from .views import user_login, user_logout, user_signup, update_password, update_info

urlpatterns = [

    path("login/", user_login, name = "login"),

    path("logout/", user_logout, name = "logout"),

    path("signup/", user_signup, name = "signup"),

    path("update-password/", update_password, name = "update-password"),

    path("update-info/", update_info, name = "update-info"),

]