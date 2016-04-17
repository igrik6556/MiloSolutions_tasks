from datetime import date


def access(user_birthday):
    """
    Checks the user's age. If more than 13,
    it allows access, otherwise blocked user.
    :param user_birthday: user birthday in
    datetime format
    :return user access
    """
    if user_birthday:
        curr_year = date.today().year
        age = curr_year - user_birthday.year
        if age > 13:
            return "Allowed"
        else:
            return "Blocked"
    else:
        return "Unknown"
