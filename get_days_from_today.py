from datetime import datetime

date_format = "%Y-%m-%d"

def get_days_from_today(date: str, today: str = "") -> int:
    """
    Кількість днів від поточної дати до вказанної.

    Parameters
    ----------
    date : str
        Cтрока дати в форматі РРРР-ММ-ДД.

    Returns
    -------
    int
        Кількість днів.
    """

    # Parse input to date object
    try:
        dt = datetime.strptime(date, date_format).date()
    # Return 0 in case of date parse error
    except ValueError as e:
        return 0

    # Create today date object
    td = datetime.today().date()

    # Calc diff from date to today
    diff = dt - td

    # Return number of days in diff
    return diff.days

if __name__ == "__main__":
    date = input(f"Введіть дату в форматі РРРР-ММ-ДД ({datetime.today().strftime(date_format)}): ")
    diff = get_days_from_today(date)
    print(f"Від сьогодні до вказанної дати {diff} днів")
