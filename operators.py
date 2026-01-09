#find if user is valid to apply for a driving license
# validation  - 18+, 75
age = int(input("Enter age"))

if age>18:
    if age<76:
        print("Valid")
    else:
        print("Not valid")
     
else:
    print("Not valid")