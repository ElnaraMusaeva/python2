x=int(input("Input of the triangle sides: \nx: "))
y=int(input("y: "))
z=int(input("z: "))
if x==y==z:
    print("Equilateral triangle")
elif x==y or y==z or x==z:
    print("Isosceles triangle")
else:
    print("Scalene triangle")