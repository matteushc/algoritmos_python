def generate_range_days(start_date, end_date, num_days, date_range_number):
    """Generate date range based on start_date and end_date. 
    Ex: start_date = 2022-04-01 and end_date = 2022-04-10 if date_range_number
    equals to 5 it will generate list with tuple like this:
        [
            ('2022-04-01', '2022-04-05'),
            ('2022-04-06', '2022-04-10'),
        ]

    Args:
        start_date (date): Start date
        end_date (date): End date
        num_days (int): Number of day between start_date and end_date
        date_range_number (int): Number of date range ex: 10

    Yields:
        [list]: List of tuples with dates range from start date to end date
    """
    for x in range(0, num_days, date_range_number):
        start = start_date + timedelta(days=x)
        end = min(end_date, start + timedelta(days=date_range_number - 1))
        yield (start, end)
