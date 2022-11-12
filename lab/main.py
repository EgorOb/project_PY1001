from random import sample
import string
from string import ascii_letters, digits


def get_random_password(n=8) -> str:
    # TODO написать функцию генерации случайных паролей
    str_ = string.ascii_letters + string.digits
    return "".join(sample(str_, n))


print(get_random_password())
