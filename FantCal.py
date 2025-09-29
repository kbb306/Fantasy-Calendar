from datetime import datetime
yearval = 0
monthval = 0
weekval = 0
while ((yearval <= 0 ) or (monthval <= 0) or (weekval <= 0)):
    weekval= int(input("How many days in a week? "))
    monthval = int(input("How many weeks in a month? "))
    yearval = int(input("How many months in a year? "))
indate = input("Enter a date: ")
try: date = datetime.strptime(indate, "%m/%d/%Y")
except ValueError:  date = datetime.strptime(indate, "%d/%m/%Y")
except ValueError:  date = datetime.strptime(indate,"%Y-%m-%d")
except ValueError: date = datetime.strptime(indate, "%Y/%m/%d")
finally: 
    print("Invalid date, falling back to today.")
    date = datetime.today()

total = (date.toordinal() - 1)
daysinyear = weekval * monthval * yearval

print("By your calender, it has been",year,"years,",month,"months,",week,"weeks and",day,"days since year 0.")
print("Your date is:",(year+"/"+month+"/"+(week*weekval + day)))

