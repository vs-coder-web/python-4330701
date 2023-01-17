from datetime import date, timedelta

def sundays(year):
    d = date(year, 1, 1) #1st January
    d += timedelta(days = 6 - d.weekday()) #First Sunday
    while d.year == year:
        yield d
        d += timedelta(days = 7)

year = int(input("Enter The Year: "))

print("Sundays List: ")

for d in sundays(year):
    print(d)