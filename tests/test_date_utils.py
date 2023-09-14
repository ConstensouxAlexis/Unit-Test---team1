from datetime import datetime
from hec.tools.date_utils import convert_to_date
def test_date_convert():
    my_date: str = "2020/09/23"
    awaited_result: datetime = datetime(2020, 9, 23)
    assert convert_to_date(my_date) == awaited_result
