print(f"List of months: January, February, March, April, May, June, July, August, September, October, Novembwer, December")
mon=input("Input the name of Month: ")
if mon=="January" or mon=="March" or mon=="May" or mon=="July"or mon=="August" or mon=="October" or mon=="December":
    print("No. of days: 31 days")
elif mon=="February":
    print("No. of days: 28/29 days")
else:
    print("No. of days: 30 days")