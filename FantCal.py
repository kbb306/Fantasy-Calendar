
import re
from datetime import date

# Gregorian calendar calculations

def is_leap(year):
    return (
        year % 4 == 0 and
        (year % 100 != 0 or year % 400 == 0)
    )


def days_in_month(year, month):
    lengths = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

    if month == 2 and is_leap(year):
        return 29

    return lengths[month - 1]


def gregorian_to_days(year, month, day):
    """
    Convert a Gregorian date to an integer.

    January 1, year 1 = day 0.
    Supports positive, negative and zero years.
    """

    if not 1 <= month <= 12:
        raise ValueError("Invalid month.")

    if not 1 <= day <= days_in_month(year, month):
        raise ValueError("Invalid day.")

    # Days in all complete preceding years.
    y = year - 1

    total = (
        365 * y
        + y // 4
        - y // 100
        + y // 400
    )

    # Days in all complete preceding months.
    for m in range(1, month):
        total += days_in_month(year, m)

    # Days elapsed in the current month.
    total += day - 1

    return total


# Date input

def parse_date(indate, isZero=False):
    indate = indate.strip()

    if not indate:
        if isZero:
            return (1, 1, 1)

        today = date.today()
        return (today.year, today.month, today.day)

    # Year-first: YYYY-MM-DD or YYYY/MM/DD
    match = re.fullmatch(
        r"([+-]?\d+)[-/](\d{1,2})[/-](\d{1,2})",
        indate
    )

    if match:
        year, month, day = map(int, match.groups())

        gregorian_to_days(year, month, day)
        return (year, month, day)

    # Month-first or day-first: MM/DD/YYYY
    match = re.fullmatch(
        r"(\d{1,2})/(\d{1,2})/([+-]?\d+)",
        indate
    )

    if match:
        a, b, year = map(int, match.groups())

        # First try MM/DD/YYYY.
        try:
            gregorian_to_days(year, a, b)
            return (year, a, b)

        except ValueError:
            # Then try DD/MM/YYYY.
            gregorian_to_days(year, b, a)
            return (year, b, a)

    raise ValueError(
        f"Unrecognized date format: {indate!r}"
    )


def parser(indate, isZero=False):
    try:
        return parse_date(indate, isZero)

    except ValueError as error:
        print("Date parsing error:", error)
        print("Falling back to default.")

        return parse_date("", isZero)
# Fantasy calendar configuration

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

# Get the epoch.
zero = parser(
    input("Enter an optional start date (Enter for standard): "),
    True
)

# Get the date to convert.
indate = input("Enter a date: ")
current = parser(indate)

# Convert both Gregorian dates into absolute day counts.
epoch_days = gregorian_to_days(*zero)
current_days = gregorian_to_days(*current)

# Calculate signed elapsed days.
total = current_days - epoch_days
elapsed = total

# Calculate the size of each fantasy calendar unit.
days_per_month = monthval * weekval
days_per_year = yearval * days_per_month

# Calculate the fantasy year.
year = total // days_per_year
total %= days_per_year

# Calculate the fantasy month.
month = total // days_per_month
total %= days_per_month

# Calculate the fantasy week.
week = total // weekval
total %= weekval

# Calculate the fantasy day.
day = total

# Convert positions to one-based numbering.
# Keep the fantasy year zero-based.
month += 1
week += 1
day += 1

# Calculate the day of the month.
day_of_month = (week - 1) * weekval + day

# Display the results.
print("Days since the epoch:", elapsed)

print(
    "Your date is:",
    str(year) + "/" +
    str(month) + "/" +
    str(day_of_month)
)
