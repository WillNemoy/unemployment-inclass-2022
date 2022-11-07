
from app.stocks import format_usd

def test_usd_formatting():
    assert format_usd(4.5) == "$4.50"
    assert format_usd(4.55555555) == "$4.56"
    assert format_usd(123456789) == "$123,456,789.00"
    #assert format_usd("OOPS") == "______"