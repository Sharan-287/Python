def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

choice = input("Choose + or -: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == "+":
    print("Result:", add(a, b))
elif choice == "-":
    print("Result:", subtract(a, b))
else:
    print("Invalid operation")
