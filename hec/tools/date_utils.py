from datetime import datetime
def convert_to_date(my_date: str):
    return datetime.strptime(my_date, '%Y/%m/%d')
