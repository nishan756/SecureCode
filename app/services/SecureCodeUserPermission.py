from app.repositories.SecureCodeUserPermission import SecureCodeUserPermissionRepo

from uuid import UUID

class SecureCodeUserPermissionService:

    def get(self, user, id:UUID):

        return SecureCodeUserPermissionRepo().get(user, id)

    def delete(self, user, id:UUID):

        return SecureCodeUserPermissionRepo().delete(user, id)