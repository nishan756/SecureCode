from app.models import SecureCodeEmailPermission

from app.exceptions import SecureCodeEmailPermissionDoesntExist

from uuid import UUID


class SecureCodeEmailPermissionRepo:


    def get(self, user, id:UUID):

        try:

            return SecureCodeEmailPermission.objects.get(secure_code__user = user, id = id)

        except SecureCodeEmailPermission.DoesNotExist:

            raise SecureCodeEmailPermissionDoesntExist()

    def delete(self, user, id:UUID):

        secure_code = self.get(user, id)

        return secure_code.delete()