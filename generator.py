import random
import string


def generate_password(length: int, num_special_chars: int, excl_chars: str):
    """
    Generate a random password with the specified number of characters,
    including special characters, and excluding certain characters.

    :param length: the number of characters in the password
    :param num_special_chars: the number of special characters to include
    :param excl_chars: a string of characters to exclude
    :return: a random password
    """
    # define the set of characters to choose from
    normal_chars = string.ascii_letters + string.digits
    # remove any characters in the excl_chars string from the chars
    normal_chars = [_ for _ in normal_chars if _ not in excl_chars]
    # randomly select characters for the password
    password = ''.join(random.choices(normal_chars, k=length - num_special_chars))
    # add random special characters
    special_chars = string.punctuation
    special_chars = [_ for _ in special_chars if _ not in excl_chars]
    password += ''.join(random.choices(special_chars, k=num_special_chars))
    # shuffle the password
    password = ''.join(random.sample(password, len(password)))
    # return the password
    return password



