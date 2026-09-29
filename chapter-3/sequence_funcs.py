# 1. range(): Numbers ki ginti generate karna
print("--- range() ---")
for num in range(1, 4):  # 1 se 3 tak
    print(num)

# 2. enumerate(): Item ke sath uska index (number) bhi dena
print("\n--- enumerate() ---")
fruits = ["Apple", "Mango", "Banana"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 3. zip(): Do alag lists ko jodi (pair) me jodhna
print("\n--- zip() ---")
names = ["Harsh", "Aman"]
marks = [95, 88]
for name, score in zip(names, marks):
    print(name, "got", score)
