num = int(input("Enter a number: "))

sum_of_squares = 0
temp = abs(num)  # handle negative numbers

while temp > 0:
    digit = temp % 10
    sum_of_squares += digit ** 2
    temp //= 10

print("Sum of squares of digits:", sum_of_squares)
