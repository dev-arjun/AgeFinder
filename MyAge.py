import datetime as dt
dob = int(input("Enter your year of birth: "))
year = dt.datetime.now().year
if dob >= 1900 and dob <= year:
    age = year - dob
    print(str(age))
else:
    print("Check your date it must be between 1900 to {0}".format(year))
