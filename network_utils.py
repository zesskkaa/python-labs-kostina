"""
Модуль для работы с IP-адресами.Содержит функции проверки, маскирования и определения частных IP.
Автор: Костина К.С.
"""

# Задание 1.1. Проверка IPv4-адреса

def validate_ip(ip):
    """Проверка корректности IPv4-адреса.
    Параметры:
    ip (str): IP-адрес для проверки.
    Возвращает:
    tuple: (bool, str) — результат проверки и сообщение об ошибке. """

    octets = ip.split(".")

    if len(octets) != 4:
        return False, "Адрес должен содержать 4 октета"

    for octet in octets:
        if octet == "":
            return False, "Октет не может быть пустым"

        if not octet.isdigit():
            return False, "ОкТеты должны содержать только цифры"

        if len(octet) > 1 and octet[0] == "0":
            return False, "Октеты не должны содержать ведущих нулей"

        number = int(octet)

        if number < 0 or number > 255:
            return False, "каждый октет должен быть от 0 до 255"

    return True, ""


# Задание 1.2. Маскирование IP-адреса

def anonymize_ip(ip, mask="XXX"):
    """
    Маскирование последнего октета IP-адреса.
    Параметры:
    ip (str): IP-адрес.
    mask (str): символы для маскирования.
    Возвращает:
    str: замаскированный IP-адрес.
    """

    result = validate_ip(ip)

    if not result[0]:
        return result[1]

    octets = ip.split(".")
    octets[3] = mask

    return ".".join(octets)


# Задание 1.3. Проверка частного IP-адреса

def is_private_ip(ip):
    """Проверка, является ли IP-адрес частным.
    Параметры:
    ip (str): IP-адрес для проверки.
    Возвращает:
    bool: True, если адрес частный, иначе False. """

    result = validate_ip(ip)

    if not result[0]:
        return False

    octets = ip.split(".")
    first = int(octets[0])
    second = int(octets[1])

    if first == 10:
        return True

    if first == 172 and 16 <= second <= 31:
        return True

    if first == 192 and second == 168:
        return True

    return False


# Тестирование модуля

if __name__ == "__main__":
    print("=== Тестирование network_utils ===")

    print(validate_ip("192.168.1.1"))
    print(validate_ip("256.168.1.1"))

    print(anonymize_ip("192.168.1.1"))
    print(anonymize_ip("10.0.0.5", "XXX"))

    print(is_private_ip("192.168.1.1"))
    print(is_private_ip("8.8.8.8"))
