import re

def normalize_phone(phone_number):
    """
    Нормалізація введеного номеру телефону.

    Parameters
    ----------
    phone_number : str
        Cтрока номера телефону.

    Returns
    -------
    str
        Нормалізовне значення номера телефону.
    """

    # Remove odd symbols
    number = re.sub(r'[^+0-9]', '', phone_number)
    # Parse number to parts
    num_info_search = re.search(r'^(?P<plus_prefix>\+)?(?P<country_code>38)?(?P<operator_code>0\d{2})(?P<number>\d{7})$', number) if number else None
    # Error if value is not in supported format
    if not num_info_search:
        raise TypeError("Номер телефону повинен мати 10 або 12 цифр та може мати знак + на початку: +38 (097) 11-22-333, 38 (097_ 11-22-333, (097) 11-22-333.")
    # Get number parts
    num_info = num_info_search.groupdict()
    # Return normilized number
    return f"+38{num_info.get('operator_code')}{num_info.get('number')}"

if __name__ == "__main__":
    # phone_number = input(f"Введіть номер телефону: ")
    # print(f"Нормалізований номер телефону: {normalize_phone(phone_number)}")
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
