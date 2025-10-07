import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Генерація необхідної кількості випадкових унікальних номерів між вказанними мінімальним та максимальним значеннями.

    Parameters
    ----------
    min : int
        Мінімальне значення від 1 до 1000.

    max : int
        Максимальне значення від 1 до 1000.

    quantity : int
        Кількість значень у списку.

    Returns
    -------
    list
        Список унікальних відсортованих випадкових номерів.
    """

    # Перевірка вхідних параметрів на коректність
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []

    numbers = set()

    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(list(numbers))

if __name__ == "__main__":
    mi = int(input(f"Введіть мінімальне число від 1 до 1000: "))
    ma = int(input(f"Введіть максимальне число від 1 до 1000: "))
    qt = int(input(f"Введіть кількість чисел для генерації: "))
    print(get_numbers_ticket(mi, ma, qt))
