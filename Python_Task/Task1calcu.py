choice = input("Choose + or - or * or /: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == "+":
    print("Result:", add(a+b))

elif choice == "-":
    print("Result:", subtract(a-b))

elif choice == "*":
    print("Result:", multiple(a*b))

elif choice == "/":
    if b==0:
        print("Division by zero is not allowed")
    else:
        print("Result:", division(a/b))

else:
    print("Invalid operation")
