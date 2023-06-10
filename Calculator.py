print("CALCULATOR".center(500))
print("------------------------".center(500))
value1 = float(input("Enter Your First Number: "))
value2 = float(input("Enter Your Second Number: "))

operator = input("Which operation do You want to use? (+,-,*,/): ")

if operator == "+":
    print(f"The Addition of the Number {value1} and {value2} is {value1 + value2}")
elif operator == "-":
    print(f"The Subtraction of the Number {value1} and {value2} is {value1 - value2}")
elif operator == "/":
    if value2 == 0:
         print("Cannot divide by zero")
    else:
        print(f"The Division of the Number {value1} and {value2} is {value1 / value2}")
elif operator == "*":
        print(f"The Multiplication of the Number {value1} and {value2} is {value1 * value2}")
else:
    print("Error! Operator not found")