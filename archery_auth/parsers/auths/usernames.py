from archery_auth.exceptions import BadUsernameError


def check_username(value):
    if value.isalpha() and len(value) > 6 and len(value) < 15:
        return value
    elif not value.isalpha():
        raise BadUsernameError(
            'Username must consist of letters and numbers.'
        )
    elif len(value) <= 6:
        raise BadUsernameError(
            'Length should be not be less than 6 characters.'
        )
    elif len(value) > 15:
        raise BadUsernameError(
            'Length should be not be longer than 15 characters.'
        )
    else:
        raise BadUsernameError(
            'Error.'
        )
