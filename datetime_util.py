import datetime


class DatetimeOperator:
    """Performs various datetime operations."""

    def __init__(self):
        pass

    def week_no(self, day, month, year) -> int:
        """Calculates the week number which was present on that date of year.

        Returns
        -------
        week_no: int
            Week number relative to that year
        """
        temp_dt = datetime.datetime(year, 1, 1)
        week_no = 0
        while (temp_dt.month < month) or (temp_dt.day < day):
            temp_dt += datetime.timedelta(days=7)
            week_no += 1

        return week_no

    def current_week_no(self) -> int:
        """Calculates the current week no of the year we are in.

        Returns
        -------
        week_no: int
            Current week no,
            example: 2nd January would come in week 1
        """
        current_dt = datetime.datetime.now()
        temp_dt = datetime.datetime(current_dt.year, 1, 1)  # start of the year
        week_no = 0

        while (temp_dt.month < current_dt.month) or (temp_dt.day < current_dt.day):
            temp_dt += datetime.timedelta(days=7)
            week_no += 1

        return week_no

    def date_of_the_week(self, week_no, year) -> datetime.datetime:
        """Calculates the date of that week_no in the year.

        Parameters
        ----------
        week_no: int
            Week no of a year

        year: int
            Year of that the weeks belongs to

        Returns
        -------
        week_dt: datetime.datetime
            Datetime object of that week_no in the year
        """
        week_dt = datetime.datetime(year, 1, 1)  # start of the year
        temp_week_no = 0

        while temp_week_no < week_no:
            week_dt += datetime.timedelta(days=7)
            temp_week_no += 1

        return week_dt

    def week_difference(self, week_no, year) -> int:
        """Calculates how many weeks ago was the given week no of that year relative to current year.

        Parameters
        ----------
        week_no: int
            Week no of a year

        year: int
            Year of that the weeks belongs to

        Returns
        -------
        week_diff: int
            Week difference
        """
        week_dt = self.week_date(week_no, year)
        temp_dt = week_dt
        current_dt = datetime.datetime.now()

        week_diff = 0

        while temp_dt < current_dt:
            temp_dt += datetime.timedelta(days=7)
            week_diff += 1

        return week_diff
