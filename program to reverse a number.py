num = int(input("Enter a number: "))

reverse = 0
temp = abs(num)   # handle negative numbers

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

# restore sign if number was negative
if num < 0:
    reverse = -reverse

print("Reversed number:", reverse)
