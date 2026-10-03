from datetime import datetime

yearval = 0
monthval = 0
weekval = 0

while yearval <= 0 or monthval <= 0 or weekval <= 0:
    try:
        weekval = int(input("How many days in a week? "))
        monthval = int(input("How many weeks in a month? "))
        yearval = int(input("How many months in a year? "))
    except ValueError:
        print("Please enter positive whole numbers.")
        continue

indate = input("Enter a date: ")

formats = ["%m/%d/%Y", "%d/%m/%Y",
           "%Y-%m-%d", "%Y/%m/%d"]

for format in formats:
    try:
        date = datetime.strptime(indate, format)
        break
    except ValueError:
        continue
else:
    print("Couldn't parse date format, falling back to today.")
    date = datetime.today()

# Convert Gregorian date into elapsed days.
total = date.toordinal() - 1

# Calculate the size of each calendar unit.
days_per_month = monthval * weekval
days_per_year = yearval * days_per_month

# Calculate the fantasy year.
year = total // days_per_year
total %= days_per_year

# Calculate the fantasy month.
month = total // days_per_month
total %= days_per_month

# Calculate the week.
week = total // weekval
total %= weekval

# Calculate the day.
day = total

# Convert from zero-based to one-based numbering.
year += 1
month += 1
week += 1
day += 1

# Calculate the day of the month.
day_of_month = (week - 1) * weekval + day

print("By your calendar, it has been",
      year - 1, "complete years,",
      month - 1, "complete months,",
      week - 1, "complete weeks and",
      day - 1, "days since the start of those periods.")

print("Your date is:",
      str(year) + "/" +
      str(month) + "/" +
      str(day_of_month))