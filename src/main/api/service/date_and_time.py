import re
from datetime import timedelta, date

class DateAndTime():
    
    @classmethod
    def is_ISO_format(cls, date: str):
        """checks if the string is in ISO format"""

        if bool(re.search("^\d{4}-\d{2}-\d{2}$", date)):
            return True
        else:
            return False
    
    @classmethod
    def get_dates_in_interval(cls, interval, initial_date, total):
        """ returns a list of dates separated by the specified interval.


        Args:
            interval (int): Amount of days that separates each date.
            initial_date (str): The first date of the list. Must be in ISO format "YYYY.MM.DD".
            total (int): The size of the list.

        Returns:
            list: List with dates separated by the specified interval. (The list starts with initial_date) 
        """

        if not cls.is_ISO_format(initial_date):
            return

        dates = list(date.fromisoformat(initial_date))
        for i in range(1, total):
            dates.append(dates[i-1] + interval)
        
        return [x.isoformat() for x in dates]
            