from archery_auth.exceptions import WrongPasswordError


def check_password(value):
    if len(value) < 6:
        raise WrongPasswordError(
            'Length should be at least 6'
        )
    elif len(value) > 50:
        raise WrongPasswordError(
            f'Length should be not be greater than 50 characters'
        )
    elif not any(char.isdigit() for char in value):
        raise WrongPasswordError(
            'Password should have at least one numeral'
        )
    elif not any(char.isupper() for char in value):
        raise WrongPasswordError(
            'Password should have at least one uppercase letter'
        )
    elif not any(char.islower() for char in value):
        raise WrongPasswordError(
            'Password should have at least one lowercase letter'
        )
    else:
        return value
