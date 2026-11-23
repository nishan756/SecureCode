from app.repositories.SecureCode import SecureCodeRepo

from django.utils import timezone

from app.exceptions import InvalidCode

from uuid import UUID


class SecureCodeService:

    def get(self, code:str):

        secure_code = SecureCodeRepo().get(code)

        if secure_code.expires_at and (timezone.now() < secure_code.expires_at):

            secure_code.is_valid = False

            secure_code.save(update_fields = ["is_valid"])

            raise InvalidCode()

        if secure_code.is_valid:

            return secure_code

        raise InvalidCode()

    def get_code_by_id(self, id:UUID):

        return SecureCodeRepo().get_code_by_id(id)

    def delete(self, user, code_id:UUID):

        secure_code = self.get_code_by_id(code_id)

        if secure_code.user == user:

            return SecureCodeRepo().delete(secure_code)

        raise PermissionError("OOPS! Can't delete this secure code object")