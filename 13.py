import datetime
g=int(input("Input a year: "))
m=int(input("Input a month [1-12]: "))
d=int(input("Input a day [1-31]: "))
x=datetime.datetime(g, m, d)
tom=x+datetime.timedelta(days=+1)
print("The next date is [yyyy-mm-dd]", tom)