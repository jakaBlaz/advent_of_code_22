from datetime import date as dt
import time as t

whole_date = dt.today()
day = whole_date.day

if 3 < day < 20:
    ordinal_number = "th"
elif day%10 == 1:
    ordinal_number = "st"
elif day%10 == 2:
    ordinal_number = "nd"
elif day%10 == 3:
    ordinal_number = "rd"
else:
    ordinal_number = "th"

month = whole_date.strftime("%B")
year = whole_date.year

print(f"Today is {day}{ordinal_number} of {month} {year}")
print("Which advent of code do you want to solve today? or press s for solutions")

if input("Please input the day number to solve or input s for solutions: ") == "s":
    print("work in progress")
else:
    print("work in progress")

