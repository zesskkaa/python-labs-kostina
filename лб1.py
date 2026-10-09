"""
Лабораторная работа №1
Студент: Костина К.С.
Группа: ОИБАС-11
Вариант: 1

Задание 1.1. Проверка IPv4-адреса
Задание 1.2. Оценка надёжности пароля
Задание 1.3. Формирование идентификатора судна
"""

import random

# Задание 1.1. проверка IPv4-адреса


def validate_ip(ip):
    """Проверка корректности IPv4-адреса.
    Параметры: ip (str): IPv4-адрес для проверки.
    Возвращает: tuple: (bool, str), где bool — результат проверки,
    str — сообщение об ошибке."""

    octets = ip.split(".")  # проверяем, что адрес состоит из 4 частей

    if len(octets) != 4:
        return False, "адрес должен содержать 4 октета"

    for octet in octets:  # проверка каждого октета
        if octet == "":
            return False, "Октет не может быть пустым"

        # проверка, что октет состоит только из цифр
        if not octet.isdigit():
            return False, "Октеты должны содержать только цифры"

        # проверка ведущих нулей
        if len(octet) > 1 and octet[0] == "0":
            return False, "Октеты не должны содержать ведущих нулей"

        # переводим октет в число
        number = int(octet)

        # проверяем диапазон
        if number < 0 or number > 255:
            return False, "Каждый октет должен быть от 0 до 255"

    return True, ""


# Задание 1.2. оценка надёжности пароля


def calculate_password_strength(password):
    """Оценка надёжности пароля.
    Параметры: password (str): пароль для проверки.
    Возвращает: str: "Надёжный", "Средний" или "Слабый"."""

    points = 0

    # проверка длины пароля
    if len(password) >= 8:
        points += 1

    # проверка наличия цифры
    has_digit = False
    for symbol in password:
        if symbol.isdigit():
            has_digit = True
            break

    if has_digit:
        points += 1

    # проверка наличия заглавной буквы
    has_upper = False
    for symbol in password:
        if symbol.isupper():
            has_upper = True
            break

    if has_upper:
        points += 1

    # проверка наличия специального символа
    special_symbols = "!@#$%^&*"
    has_special = False
    for symbol in password:
        if symbol in special_symbols:
            has_special = True
            break

    if has_special:
        points += 1

    # определяем результат по количеству баллов
    if points == 4:
        return "Надёжный"
    elif points >= 2:
        return "Средний"
    else:
        return "Слабый"


# Задание 1.3. Формирование идентификатора судна


def generate_vessel_id(name, registration_year, random_suffix=True):
    """Формирование идентификатора судна.
    Параметры: name (str): название судна.
    registration_year (int): год регистрации.
    random_suffix (bool): добавлять ли случайный суффикс.
    Возвращает: str: сформированный идентификатор судна."""

    # берём первые 3 буквы названия
    vessel_name = name[:3].upper()

    # берём последние 2 цифры года
    year = str(registration_year)[-2:]

    # формируем основную часть идентификатора
    vessel_id = vessel_name + year

    # если random_suffix=True, добавляем случайное число
    if random_suffix:
        suffix = random.randint(100, 999)
        vessel_id = vessel_id + "-" + str(suffix)

    return vessel_id


# Демонстрация работы функций

if __name__ == "__main__":
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ФУНКЦИЙ (ВАРИАНТ 1)")
    print("=" * 60)

    # демонстрация функции 1
    print("\n--- Задание 1.1. validate_ip ---")
    test_ips = ["192.168.1.1","256.168.1.1","192.168.01.1","192.168.1","192.abc.1.1"]

    for ip in test_ips:
        result = validate_ip(ip)
        print(f"validate_ip('{ip}') → {result}")

    # демонстрация функции 2
    print("\n--- Задание 1.2. calculate_password_strength ---")
    test_passwords = ["Password123!", "Password", "pass123", "abc"]

    for password in test_passwords:
        result = calculate_password_strength(password)
        print(f"calculate_password_strength('{password}') → {result}")

    # демонстрация функции 3
    print("\n--- Задание 1.3. generate_vessel_id ---")
    vessel_id_1 = generate_vessel_id("Titanic", 2024)
    print(f"generate_vessel_id('Titanic', 2024) → {vessel_id_1}")

    vessel_id_2 = generate_vessel_id("Aurora", 2023, random_suffix=False)
    print(f"generate_vessel_id('Aurora', 2023, False) → {vessel_id_2}")














    
