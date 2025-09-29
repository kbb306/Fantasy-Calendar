from datetime import datetime
yearval, monthval,weekval = 0
while ((yearval <= 0 ) or (monthval <= 0) or (weekval <= 0)):
    weekval= input("How many days in a week? ")
    monthval = input("How many weeks in a month? ")
    yearval = input("How many months in a year? ")
indate = input("Enter a date: ")
try:  date = datetime.strptime(indate, "%d/%m/%Y")
except ValueError:  date = datetime.strptime(indate,"%Y-%m-%d")
except ValueError: date = datetime.strptime(indate, "%Y/%m/%d")
finally: date = input("Invalid date, please try again: ")

total = date.toordinal() - 1

year = total // yearval
total %= yearval
month = total // monthval
total %= monthval
week = total // weekval
total %= weekval
day = total 
print("By your calender, it has been",year,"years,",month,"months,",week,"weeks and",day,"days since year 0.")
print("Your date is:",(year+"/"+month+"/"+(week*weekval + day)))

