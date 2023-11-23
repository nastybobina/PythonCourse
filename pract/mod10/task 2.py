import re
import doctest


def color_check(color):
    """
        Функция проверяет строку web-цветов на корретность целиком

        Args:
        color(str): строка для ввода цветов

        Returns:
            bool: True - строка является корректным цветом, False - строка является некорректным цветом

        >>> color_check("#21f48D")
        True
        >>> color_check("#666")
        True
        >>> color_check("rgb(255, 255, 255)")
        True
        >>> color_check("rgb(10%, 20%, 0%)")
        True
        >>> color_check("hsl(0, 0%, 0%)")
        True
        >>> color_check("#23456")
        False
        >>> color_check("aaaaaaaaaa")
        False
        >>> color_check("rgb(257, 51, 4530)")
        False
        >>> color_check("hsl(223, 10, 0.5)")
        False
        >>> color_check("hsl(323%, 20%, 50%)")
        False
        >>> color_check("hsl(200, 100%, 50%)")
        True
                >>> color_check("rgb(255, 255,255)") # это и следующие тесты - проверка на верный ввод пробела/запятой цветов, так как в примере был такой ввод
        True
        >>> color_check("rgb(255,255, 255)") # то же
        True
        >>> color_check("rgb(255,255,255)") # то же
        True
        >>> color_check("rgb(14%,23%, 0%)") # то же
        True
        >>> color_check("rgb(10%, 20%,0%)") # то же
        True
        >>> color_check("rgb(30%,12%,0%)") # то же
        True
        >>> color_check("hsl(200,100%, 50%)") # то же
        True
        >>> color_check("hsl(200, 100%,50%)") # то же
        True
        >>> color_check("hsl(200,100%,50%)") # то же
        True
        """

    # HEX формат
    hex_color_pattern = re.compile(r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')

    # RGB формат
    rgb_color_pattern = re.compile(r'^\s*rgb\s*\(\s*((\d{1,2}%|100%?)|'
                                   r'([01]?\d{1,2}|2[0-4]\d|25[0-5]))\s*,\s*((\d{1,2}%|100%?)'
                                   r'|([01]?\d{1,2}|2[0-4]\d|25[0-5]))\s*,\s*((\d{1,2}%|100%?)'
                                   r'|([01]?\d{1,2}|2[0-4]\d|25[0-5]))\s*\)\s*$')

    # HSL формат
    hsl_color_pattern = re.compile(r'^hsl\((\d{1,3}|[1-9]\d?|[12]\d{2}|3[0-5]\d),'
                                   r'\s*(100%|[1-9]\d?%|0%),\s*(100%|[1-9]\d?%|0%)\)$')

    return hex_color_pattern.search(color) is not None or \
        rgb_color_pattern.search(color) is not None or \
        hsl_color_pattern.search(color) is not None


doctest.testmod()
