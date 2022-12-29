from datetime import datetime


class MyDatetime:
    @staticmethod
    def get_tuple_datetime(date: dict) -> tuple:
        return (
            int(date["year"]),
            int(date["month"]),
            int(date["day"]),
            int(date["hour"]),
            int(date["minute"]),
            int(date["second"]),
        )

    @staticmethod
    def get_str_for_dict_date(date: dict) -> str:
        result_date = str(
            datetime(
                date["year"],
                date["month"],
                date["day"],
                date["hour"],
                date["minute"],
                date["second"],
            )
        )
        return result_date

    @staticmethod
    def get_datetime(date: dict) -> datetime:
        return datetime(
            date["year"],
            date["month"],
            date["day"],
            date["hour"],
            date["minute"],
            date["second"],
        )
