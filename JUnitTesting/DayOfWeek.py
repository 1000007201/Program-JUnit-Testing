
def day_of_week(day, month, year):
    _year = year - (14 - month)//12
    x = _year + _year//4 - _year//100 + _year//400
    _month = month + 12 * ((14 - month)//12) - 2
    _day = (day + x + 31*_month//12) % 7
    return _day


dict1 = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
day_out = day_of_week(17, 12, 1998)
print(dict1.get(day_out))
