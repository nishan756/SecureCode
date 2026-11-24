from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .exceptions import SecureCodeDoesNotExists, InvalidCode

from uuid import UUID

from django.contrib import messages

from .serializers import SecureCodeSerializer, OriginalURLSerializer

from rest_framework import permissions

from rest_framework.decorators import permission_classes, api_view

from rest_framework.response import Response

from rest_framework import status

from app.services.SecureCode import SecureCodeService


def home(request):

    return render(request, "home.html")

@api_view(["GET"])
def get_code(request, code:str):

    try:
    
        secure_code = SecureCodeService().get(code)

        serializer  = OriginalURLSerializer(instance = {"original_url":secure_code.original_url})

        return Response(serializer.data, status = status.HTTP_200_OK)
        

    except SecureCodeDoesNotExists as e:

        return Response({"message":str(e)}, status = status.HTTP_404_NOT_FOUND)

    except InvalidCode as e:

        return Response({"message":str(e)}, status = status.HTTP_403_FORBIDDEN)

    except Exception as e:

        return Response({"message":"Something unexpected happened"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_code(request):
    
    serializer = SecureCodeSerializer(data = request.data)

    if serializer.is_valid():


        serializer.save(user = request.user)

        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_code(request, id:UUID):
    
    try:
        
        SecureCodeService().delete(user = request.user, code_id =  id)

        return Response({"message":"Successfully deleted your code"}, status = status.HTTP_204_NO_CONTENT)

    except SecureCodeDoesNotExists as e:

        return Response({"message":str(e)}, status = status.HTTP_404_NOT_FOUND)

    except PermissionError as e:

        return Response({"message":str(e)}, status = status.HTTP_403_FORBIDDEN)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def my_codes(request):

    secure_codes = SecureCodeService().get_all_codes(request.user)

    serializer = SecureCodeSerializer(secure_codes, many = True)

    return Response(serializer.data, status = status.HTTP_200_OK)