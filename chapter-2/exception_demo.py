# 1. try, except, aur finally
num = 10
divisor = 0

try:
    # Yahan shaq hai ki zero division error aa sakti hai
    result = num / divisor
    print("Result:", result)

except ZeroDivisionError:
    # Agar error aayi toh program crash nahi hoga, ye chalega
    print("Error: It is not possible to divide by zero!")

finally:
    # Ye line chahe error aaye ya na aaye, hamesha chalegi
    print("Process complete!")


# 2. raise (Apni taraf se error trigger karna)
age = -5

if age < 0:
    print("\nCustom Check:")
    # Hum khud error trigger kar rahe hain
    # (Comment hata kar dekh sakte ho run karne ke liye)
    # raise ValueError("Age negative nahi ho sakti!")
    print("Warning: Age is negative.")
