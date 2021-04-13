life = 90
age = int(input("Enter your age: "))
days = (life - age) * 365
weeks = (life - age) * 52
months = (life - age) * 12

print(f"You have {days} days, {weeks} weeks, or {months} months left.")
