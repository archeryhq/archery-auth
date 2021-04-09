class LogInError(Exception):
    def __init__(
        self: object,
        username: str
    ) -> None:
        self.username = username

    def __str__(self) -> str:
        return f'Error in authorization of person { self.username }!'


class WrongPasswordError(Exception):
    def __init__(
        self: object,
        reason: str
    ) -> None:
        self.reason = reason

    def __str__(self) -> str:
        return self.reason


class BadUsernameError(Exception):
    def __init__(
        self: object,
        value: str
    ) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value


class EmailError(Exception):
    def __init__(
        self: object,
        value: str
    ) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'Value { self.value } not is a valid email.'
