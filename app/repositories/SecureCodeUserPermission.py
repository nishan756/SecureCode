from app.models import SecureCodeUserPermission

from app.exceptions import SecureCodeUserPermissionDoesnotExist

from uuid import UUID

class SecureCodeUserPermissionRepo:

    def get(self, user, id:UUID):

        try:

            return SecureCodeUserPermission.objects.get(user = user, id = id)

        except SecureCodeUserPermission.DoesNotExist:

            raise SecureCodeUserPermissionDoesnotExist()

    def delete(self, user, id:UUID):

        user_perm = self.get(user, id)

        return user_perm.delete()