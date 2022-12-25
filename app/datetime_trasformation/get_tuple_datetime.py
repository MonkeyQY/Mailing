from datetime import datetime


class MyDatetime:

    @staticmethod
    def get_tuple_datetime(date: dict) -> tuple:
        return int(date.get("year")), \
            int(date.get("month")), \
            int(date.get("day")), \
            int(date.get("hour")), \
            int(date.get("minute")), \
            int(date.get("second"))

    @staticmethod
    def get_str_for_dict_date(date: dict) -> str:
        result_date = str(
            datetime(
                date['year'],
                date['month'],
                date['day'],
                date['hour'],
                date['minute'],
                date['second']))
        return result_date

    @staticmethod
    def get_datetime(date: dict) -> datetime:
        return datetime(
            date['year'],
            date['month'],
            date['day'],
            date['hour'],
            date['minute'],
            date['second'])
