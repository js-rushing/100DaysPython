def is_leap(year):
    if (year % 4 == 0 & year % 100 != 0):
        return True
    elif (year % 4 == 0 & year % 100 == 0 & year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = month_days[month-1]
    if (is_leap(year) and month == 2):
        result += 1
    return result


# Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
