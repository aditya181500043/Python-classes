# Program to find sum of first n natural numbers using while loop

n = int(input("Enter a natural number: "))
sum_n = 0
i = 1

while i <= n:
    sum_n += i
    i += 1

print("Sum of first", n, "natural numbers is:", sum_n)

