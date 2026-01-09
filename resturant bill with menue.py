dal = 70
Mix_veg = 70
rice = 90

a = input("Enter food ")
b = int(input("Enter quantity"))

if a == "dal":
    price = 70
elif a == "Mix veg":
    price = 70
elif a == "rice":
    price = 90


print("========Bill========")
print(a,"x",b,"= Rs",price*b)