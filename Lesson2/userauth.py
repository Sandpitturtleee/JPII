class UserNotFoundError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class UserAuth:
    def __init__(self, users: dict):
        self.users = users

    def login(self, username: str, password: str):
        if username not in self.users:
            raise UserNotFoundError("User not found")
        if self.users[username] != password:
            raise WrongPasswordError("Wrong password")
        return "Login successful"
