from datetime import timedelta, datetime
from typing import List

DATE_FORMAT = "%Y-%m-%d"


def get_dates_range(start_date: datetime, end_date: datetime) -> List[datetime]:
    day_count = (end_date - start_date).days

    dates = []
    for day in range(day_count):
        dates.append(start_date + timedelta(day))

    return dates


def add_days(date: datetime, number_days: int) -> datetime:
    return date + timedelta(number_days)
