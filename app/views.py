from django.shortcuts import render

from .exceptions import SecureCodeDoesNotExists, InvalidCode, SecureCodeUserPermissionDoesnotExist, SecureCodeEmailPermissionDoesntExist

from uuid import UUID

from .serializers import SecureCodeSerializer, OriginalURLSerializer, SecureCodeUserPermissionSerializer, SecureCodeEmailPermissionSerializer

from rest_framework import permissions

from rest_framework.decorators import permission_classes, api_view

from rest_framework.response import Response

from rest_framework import status

from app.services.SecureCode import SecureCodeService

from app.services.SecureCodeUserPermission import SecureCodeUserPermissionService

from app.services.SecureCodeEmailPermission import SecureCodeEmailPermissionService

from app.models import SecureCode


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

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def add_user_permission(request, id:UUID):
    
    user_perm = request.data

    try:

        secure_code = SecureCodeService().get_code_by_id(id)

    except SecureCodeDoesNotExists as e:

        return Response({"message":e}, status = status.HTTP_404_NOT_FOUND)

    if secure_code.user != request.user:

        return Response({"message":"OOPS! You can't add user for this code"}, status = status.HTTP_403_FORBIDDEN)

    user_perm["secure_code"] = secure_code.id

    serializer = SecureCodeUserPermissionSerializer(data = user_perm)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_user_permission(request, id:UUID):
    
    try:
        
        SecureCodeUserPermissionService().delete(request.user, id)

        return Response({"message":"Successfully deleted user permission"}, status = status.HTTP_204_NO_CONTENT)

    except SecureCodeUserPermissionDoesnotExist as e:

        return Response({"message":str(e)}, status = status.HTTP_404_NOT_FOUND)

    except Exception as e:

        return Response({"message":"Something unexpected happened"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def add_email_permission(request, id:UUID):
    
    try:

        secure_code = SecureCodeService().get_code_by_id(id)

        if secure_code.user == request.user:

            data = request.data

            data = data.copy()

            data["secure_code"] = secure_code.id

            serializer = SecureCodeEmailPermissionSerializer(data = data)

            if serializer.is_valid():

                serializer.save()

                return Response(serializer.data, status = status.HTTP_201_CREATED)

            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        return Response({"message":"You can't perform this operation"}, status = status.HTTP_403_FORBIDDEN)

    except SecureCodeDoesNotExists as e:

        return Response({"message":str(e)}, status = status.HTTP_404_NOT_FOUND)

    except Exception as e:

        return Response({"message":"Something unexpected happened while processing this request"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_email_permission(request, id:UUID):
    
    try:

        SecureCodeEmailPermissionService().delete(request.user, id)

        return Response({"message":"Successfully deleted email permission"}, status = status.HTTP_204_NO_CONTENT)
    
    except SecureCodeEmailPermissionDoesntExist as e:

        return Response({"message":str(e)}, status = status.HTTP_404_NOT_FOUND)
    
    except Exception as e:

        print(str(e))

        return Response({"message":"Something unexpected happened"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR) 

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

@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_multiple_code(request):
    
    selected_ids = request.data.get("selected_ids");

    if selected_ids and isinstance(selected_ids, list):

        SecureCode.objects.filter(id__in = selected_ids, user = request.user).delete()

        return Response({"message":"Successfully deleted your secure codes"}, status = status.HTTP_204_NO_CONTENT)

    elif not selected_ids:
        return Response({"message":"Please provide one or more id"}, status = status.HTTP_400_BAD_REQUEST)

    elif not isinstance(selected_ids, list):

        return Response({"message":"Please parse a id list"}, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def my_codes(request):

    secure_codes = SecureCodeService().get_all_codes(request.user)

    serializer = SecureCodeSerializer(secure_codes, many = True)

    return Response(serializer.data, status = status.HTTP_200_OK)