from datetime import datetime
from project import verify_data, format_date, format_time, validate_mode, validate_RST, validate_freq

def test_verify_data_1():
    assert verify_data("TEST", "CW", "3.5", "418", "599") == 0
    assert verify_data("TEST", "SSB", "3.5", "418", "599") == 0
    assert verify_data("TEST", "CW", "3.5", "519", "559") == 0
    assert verify_data("TEST", "SSB", "21", "418", "599") == 0
    assert verify_data("TEST", "CW", "3.5", "599", "599") == 0

def test_verify_data_2():
    assert verify_data("TEST", "MORSE", "3.5", "418", "599") == 1
    assert verify_data("TEST", "CW", "5.5", "418", "599") == 1
    assert verify_data("TEST", "CW", "3.5", "699", "599") == 1
    assert verify_data("TEST", "none", "4.5", "418", "599") == 2
    assert verify_data("TEST", "DIGITAL", "7.074", "509", "599") == 3

def test_format_date():
    assert format_date("2023-06-16") == "2023-06-16"
    assert format_date("") == datetime.utcnow().date().strftime("%Y-%m-%d")
    assert format_date("6/12/23") == datetime.utcnow().date().strftime("%Y-%m-%d")
    assert format_date("13/15/2023") == datetime.utcnow().date().strftime("%Y-%m-%d")
    assert format_date("cat") == datetime.utcnow().date().strftime("%Y-%m-%d")
    assert format_date("date") == datetime.utcnow().date().strftime("%Y-%m-%d")
    assert format_date("12/15/2045") == datetime.utcnow().date().strftime("%Y-%m-%d")
    assert format_date("2023-12-15") == "2023-12-15"

def test_format_time():
    assert format_time("11:23") == "11:23"
    assert format_time("21:23") == "21:23"
    assert format_time("15:23") == "15:23"
    assert format_time("15:67") == datetime.utcnow().strftime("%H:%M")
    assert format_time("24:17") == datetime.utcnow().strftime("%H:%M")
    assert format_time("25:17") == datetime.utcnow().strftime("%H:%M")
    assert format_time("25:17") == datetime.utcnow().strftime("%H:%M")

def test_validate_mode():
    assert validate_mode("CW") == 0
    assert validate_mode("SSB") == 0
    assert validate_mode("Digital") == 0
    assert validate_mode("cw") == 1
    assert validate_mode("Dig") == 1
    assert validate_mode("FT8") == 1

def test_validate_freq():
    assert validate_freq("1.6") == 0
    assert validate_freq("7") == 0
    assert validate_freq("14") == 0
    assert validate_freq("144") == 0
    assert validate_freq("1.5") == 1
    assert validate_freq("5.5") == 1
    assert validate_freq("7.0") == 1
    assert validate_freq("cat") == 1
    assert validate_freq(21) == 1

def test_validate_rst():
    assert validate_RST("599") == 0
    assert validate_RST("519") == 0
    assert validate_RST("428") == 0
    assert validate_RST("59") == 0
    assert validate_RST("51") == 0
    assert validate_RST("42") == 0
    assert validate_RST(59) == 1
    assert validate_RST(599) == 1
    assert validate_RST("509") == 1
    assert validate_RST("699") == 1
    assert validate_RST("50") == 1
    assert validate_RST("73") == 1
    assert validate_RST("cat") == 1
