# Program 4.2: Find Total and Average of 3 Numbers

# 1. User se 3 numbers input lena (float taaki decimals bhi support kare)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# 2. Total calculate karna
total = num1 + num2 + num3

# 3. Average calculate karna
average = total / 3

# 4. Result print karna
print("\n--- Result ---")
print("Total Sum :", total)
print("Average   :", round(average, 2))  # 2 decimal places tak round off
