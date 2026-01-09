a = int(input("Enter first side"))
b = int(input("Enter second side"))
c = int(input("Enter third side"))

sides = sorted([a,b,c])
p, b, h = sides

if h**2 == p**2 + b**2:
    print("The sides form a right triangle")
else:
    print("The sides do not form a right triangle")