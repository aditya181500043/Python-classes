name = input("Enter name ")
age = int(input("Enter age "))
category = input("Enter class ")
distance =int(input("Enter distance travelled "))

base_fare = 0.50
fare = distance * base_fare

# print(type(name))
# print(type(age))
# print(type(base_fare))

if category!="Sleeper" and category!="AC" and category!="FirstClass":
    print("Invalid category")
else:
    print("Passenger name:",name)
    print("Passenger age:",age)
    print("Total distance:",distance)
    if(category=="Sleeper"):
        print("Total fare (Sleeper):",fare)
    elif(category=="AC"):
        fare = fare*2
        print("Total fare (AC):",fare)
    else:
        fare = fare*3
        print("Total fare (FirstClass):",fare)
        
    if(age>=60):
        fare = fare*.6
    elif(age<5):
        fare = 0
    elif(age>=5 and age<=12):
        fare = fare / 2

    print("Final amount:",fare)