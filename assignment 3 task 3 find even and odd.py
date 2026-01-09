num = int(input("Enter number "))
even_count = 0
odd_count = 0

while num>0:
    digit = num%10
    if digit%2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num //=10

print("Even digits: ",even_count)
print("Odd digits: ",odd_count)    