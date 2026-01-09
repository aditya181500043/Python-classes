a = int(input("Enter units "))

if a<=100:
   fare = a*1.5
elif a>=100 and a<=200:
   fare = a*2.5
elif a>200:
   fare = a*3.5

print("========Bill========")
print("Fare ", fare)