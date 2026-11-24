from app.repositories.SecureCodeEmailPermission import SecureCodeEmailPermissionRepo
from uuid import UUID


class SecureCodeEmailPermissionService:


    def get(self, user, id:UUID):

        return SecureCodeEmailPermissionRepo().get(user, id)

    def delete(self, user, id:UUID):

        return SecureCodeEmailPermissionRepo().delete(user, id)