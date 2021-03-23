year = int(input("Enter the year: "))
is_isnt = "is"
if (year % 4 == 0 & year % 100 != 0):
    is_isnt = "is"
elif (year % 4 == 0 & year % 100 == 0 & year % 400 == 0):
    is_isnt = "is"
else:
    is_isnt = "isn't"
print(f"{year} {is_isnt} a leap year.")
