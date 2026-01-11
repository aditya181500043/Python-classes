num = int(input("Enter a number: "))

temp = abs(num)  # handle negative numbers

while temp >= 10:
    sum_of_digits = 0
    while temp > 0:
        sum_of_digits += temp % 10
        temp //= 10
    temp = sum_of_digits

print("Digital root:", temp)
