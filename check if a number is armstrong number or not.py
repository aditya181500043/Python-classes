num = int(input("Enter a number: "))

if num <= 0:
    print("The number is not a perfect number.")
else:
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        print("The number is a perfect number.")
    else:
        print("The number is not a perfect number.")
