import math

# Accept a floating-point number from the user
num = float(input("Enter a floating-point number: "))

# Display the results
print("\n--- Mathematical Operations ---")
print("1. Square          :", num ** 2)
print("2. Cube            :", num ** 3)
print("3. Square Root     :", math.sqrt(num))
print("4. Ceiling Value   :", math.ceil(num))
print("5. Floor Value     :", math.floor(num))
print("6. Absolute Value  :", abs(num))
print("7. Type of Variable:", type(num))
print("8. Memory Address  :", id(num))
