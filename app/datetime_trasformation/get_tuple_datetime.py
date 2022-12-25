class MyDatetime:

    @staticmethod
    def get_tuple_datetime(date: dict) -> tuple:
        return int(date.get("year")), \
            int(date.get("month")), \
            int(date.get("day")), \
            int(date.get("hour")), \
            int(date.get("minute")), \
            int(date.get("second"))
