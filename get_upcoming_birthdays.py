from datetime import datetime, timedelta

date_format = "%Y.%m.%d"

def get_upcoming_birthdays(users):
    """
    Прийдешні дні народження.

    Parameters
    ----------
    users : list
        Список словарів з полям імʼя та день народження.

    Returns
    -------
    list
        Список словарів для користувачів, чий день народження буде у найбліжчі 7 днів.
    """

    # Get today and closest Sunday
    today = datetime.today().date()
    week_later = today + timedelta(days=7)
    # Create empty list
    result = list()
    # Process users
    for u in users:
        # Parse original date
        birthday = datetime.strptime(u["birthday"], date_format).date()
        # Use same month and day but this year
        birthday_this_year = datetime.strptime(f"{today.year}.{birthday.month}.{birthday.day}", date_format).date()
        # If it happened this year, then try next year
        if birthday_this_year < today:
            birthday_this_year += timedelta(days=365)
        # Skip birthdays outside of 7 days ahead interval
        if birthday_this_year > week_later:
            continue
        # If it is Sat or Sun, then try Mon
        if birthday_this_year.weekday() > 4:
            birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
        # Add user notification info to the list
        result.append({'name': u['name'], 'congratulation_date': birthday_this_year.strftime(date_format)})
    return result

if __name__ == "__main__":
    # Get today and calculate next weekend
    today = datetime.today().date()
    friday = today + timedelta(days=((4 - today.weekday() + 7) % 7))
    saturday = friday + timedelta(days=1)
    sunday = saturday + timedelta(days=1)
    # Generate user info list
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Next Friday", "birthday": f"{friday.year}.{friday.month:02d}.{friday.day:02d}"},
        {"name": "Next Saturday", "birthday": f"{saturday.year}.{saturday.month:02d}.{saturday.day:02d}"},
        {"name": "Next Sunday", "birthday": f"{sunday.year}.{sunday.month:02d}.{sunday.day:02d}"}
    ]
    # Show input and the result
    print("Список днів народження:", users)
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
