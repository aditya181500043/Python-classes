num = int(input("Enter a number: "))

temp = abs(num)  # handle negative numbers
product = 1

if temp == 0:
    product = 0  # product of digits of 0 is 0
else:
    while temp > 0:
        digit = temp % 10
        product *= digit
        temp //= 10

print("Product of all digits:", product)
