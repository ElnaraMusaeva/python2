lst=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Novembwer", "December"]
m=int(input("Input the month (e.g. [1-12]): "))
d=int(input("Input the day: "))
if m==1 or m==2 or m==12:
    print(f"Output: {lst[m-1]}, {d}. Season is winter")
elif 3<=m<=5:
    print(f"Output: {lst[m-1]}, {d}. Season is spring")
elif 6<=m<=8:
    print(f"Output: {lst[m-1]}, {d}. Season is summer")
else:
    print(f"Output: {lst[m-1]}, {d}. Season is autumn")