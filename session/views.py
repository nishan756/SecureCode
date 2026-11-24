from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate

from rest_framework import status, permissions

from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes

from .serializers import UserLoginSerializer, UserSignupSerializer, UserUpdateSerializer, UserPasswordUpdateSerializer, UserSerializer

from django.contrib.auth import get_user_model 

User = get_user_model()


@api_view(["POST"])
def user_login(request):

    if request.user.is_authenticated:

        return Response({"message":"Already Authenticated"}, status = status.HTTP_200_OK)

    serializer = UserLoginSerializer(data = request.data)

    if serializer.is_valid():

        username = serializer.validated_data.get("username")

        password = serializer.validated_data.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:

            login(request, user)

            return Response({"message":"Login Successfull"}, status = status.HTTP_200_OK)

        return Response({"message":"Invalid Username or Password"}, status = status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def user_logout(request):
    
    if request.user.is_authenticated:

        logout(request)

        return Response({"message":"Logout Successfull"}, status = status.HTTP_200_OK)

    return Response({"message":"User not authenticated"}, status = status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def user_signup(request):
    
    if request.user.is_authenticated:
        
        return Response({"message":"You're authenticated. To create a new account, you must logout from this session"}, status = status.HTTP_403_FORBIDDEN)

    serializer = UserSignupSerializer(data = request.data)

    if serializer.is_valid():

        serializer.save()

        return Response({"message":"Successfully created your account"}, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def update_password(request):

    serializer = UserPasswordUpdateSerializer(data = request.data)

    if serializer.is_valid():
        
        old_password = serializer.validated_data.pop("old_password")

        new_password = serializer.validated_data.pop("new_password")
        
        if not request.user.check_password(old_password):
        
            return Response({"message":"Wrong old password"}, status = status.HTTP_400_BAD_REQUEST)
        
        user = request.user

        user.set_password(new_password)
        
        user.save(update_fields = ["password"])

        return Response({"message":"Successfully updated your password"}, status = status.HTTP_200_OK)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def update_info(request):

    user = request.user

    serializer = UserUpdateSerializer(instance = user, data = request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status = status.HTTP_200_OK)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_users(request):
    
    username = request.GET.get("username", None)

    if not username:

        return Response({"message":"You must provide username"})

    users = User.objects.filter(username__icontains = username)

    serializer = UserSerializer(users, many = True)

    return Response(serializer.data, status = status.HTTP_200_OK)