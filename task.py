# Ask for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Avoid division by zero
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")
