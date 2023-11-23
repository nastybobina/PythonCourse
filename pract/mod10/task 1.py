import re
import doctest


def correct_password_check(user_password):
    """
    Функция проверяет пароль на корректность

    Args:
    password(str): Пароль

    Returns:
        bool: True - введеные данные являются корректным паролем, False - не является

    >>> correct_password_check('rtG3FG!Tr^e')
    True
    >>> correct_password_check('aA1!*!1Aa')
    True
    >>> correct_password_check('oF^a1D@y5e6')
    True
    >>> correct_password_check('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> correct_password_check('пароль')
    False
    >>> correct_password_check('password')
    False
    >>> correct_password_check('qwerty')
    False
    >>> correct_password_check('lOngPa$$$W0Rd')
    False
    >>> correct_password_check('dasfasdfds')
    False
    >>> correct_password_check('21323452345')
    False
    >>> correct_password_check('P9BVmYLZgLtW')
    False
    """

    password_conditions = (
        # пароль состоит из правильных символов и длина не менее 6
        r'^(?=[A-Za-z\d^$%@#&*!?]{6,}$)'
        # пароль содержит как минимум одно число/цифру
        r'(?=.*\d)'
        # пароль содержит как минимум 2 символа в верхнем регистре
        r'(?=.*[A-Z].*[A-Z])'
        # пароль содержит как минимум два разных спецсимвола
        r'(?=.*[!@#$%^&*?])'        
        # пароль не содержит три одинаковых символа подряд
        r'(?!.*(.)\1\1)'
    )

    return bool(re.match(password_conditions, user_password))


doctest.testmod()
