class SecureCodeDoesNotExists(Exception):

    def __init__(self):

        self.message = "This code doesn't exist"

        super().__init__(self.message)


class InvalidCode(Exception):

    def __init__(self):

        self.message = "This code is invalid"

        super().__init__(self.message)


class InvalidVivibility(Exception):

    def __init__(self):

        self.message = "Please provide a valid visibility. They're either public or private"

        super().__init__(self.message)