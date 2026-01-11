num = int(input("Enter a number: "))

temp = abs(num)  # handle negative numbers
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

# compare original number (absolute value) with reversed number
if abs(num) == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
