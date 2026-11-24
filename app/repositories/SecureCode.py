from app.models import SecureCode

from django.contrib.auth import get_user_model as User

from app.exceptions import InvalidVisibility, SecureCodeDoesNotExists

from datetime import datetime

from uuid import UUID

class SecureCodeRepo:

    def get(self, code:str):
        
        try:

            return SecureCode.objects.get(code = code)

        except SecureCode.DoesNotExist:

            raise SecureCodeDoesNotExists()


    def get_code_by_id(self, id:UUID):

        try:

            return SecureCode.objects.get(id = id)

        except SecureCode.DoesNotExist:

            raise SecureCodeDoesNotExists()


    def get_sll_codes(self, user:User):

        return SecureCode.objects.filter(user = user)


    def delete(self, secure_code:SecureCode):
            
        return secure_code.delete()