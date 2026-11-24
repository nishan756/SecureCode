class SecureCodeDoesNotExists(Exception):

    def __init__(self):

        self.message = "This code doesn't exist"

        super().__init__(self.message)


class InvalidCode(Exception):

    def __init__(self):

        self.message = "This code is invalid"

        super().__init__(self.message)


class InvalidVisibility(Exception):

    def __init__(self):

        self.message = "Please provide a valid visibility. They're either public or private"

        super().__init__(self.message)


class SecureCodeUserPermissionDoesnotExist(Exception):

    def __init__(self):

        self.message = "User permission doesn't exsists"

        super().__init__(self.message)

class SecureCodeEmailPermissionDoesntExist(Exception):

    def __init__(self):

        self.message = "Email permission doesn't exists"

        super().__init__(self.message)