for i in range(8):
    for j in range(5):
        if (i==0 or i==3) and (j>0 and j<4) or (j==0 and (i >=0 and i<7)) or (j==4 and (i >0 and i<3)) or (j==2 and (i>3 and i<5)) or (j==3 and (i >4 and i<6)) or (j==4 and (i >5 and i<7)):
            print("*", end="")
        else:
            print(end=" ")
    print()