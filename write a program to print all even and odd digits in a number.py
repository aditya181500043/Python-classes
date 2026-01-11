num = int(input("Enter a number: "))

even_count = 0
odd_count = 0
temp = abs(num)  # handle negative numbers

if temp == 0:
    even_count = 1  # 0 is considered even

while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    temp //= 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)
