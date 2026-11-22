class SecureCodeDoesNotExists(Exception):

    def __init__(self):

        self.message = "This code doesn't exist"

        super().__init__(self.message)