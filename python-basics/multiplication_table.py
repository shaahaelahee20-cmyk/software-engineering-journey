# Learning Python loops

number = int(input("Enter a number: "))

print("\n--- Multiplication Table ---")

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)
