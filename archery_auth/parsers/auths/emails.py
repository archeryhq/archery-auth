from archery_auth.exceptions import EmailError
from re import compile


def check_email(value):
    regex = compile(
        r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    )
    if regex.match(value):
        return value
    else:
        raise EmailError(value)
