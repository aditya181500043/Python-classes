n = int(input("n = "))

x = n%3
y = n%5

if x == 0 and y == 0:
    print("Fizz Buzz")
elif x == 0:
    print("Fizz")
elif y == 0:
    print("buzz")
else:
    print(n)
