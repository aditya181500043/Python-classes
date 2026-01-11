num = int(input("Enter a number: "))

temp = abs(num)  # handle negative numbers

# Initialize a dictionary to store count of each digit
digit_count = {i: 0 for i in range(10)}

# Special case: if the number is 0
if temp == 0:
    digit_count[0] = 1

# Count digits
while temp > 0:
    digit = temp % 10
    digit_count[digit] += 1
    temp //= 10

# Print the count of each digit
for digit in range(10):
    if digit_count[digit] > 0:
        print(f"Digit {digit} appears {digit_count[digit]} time(s)")
