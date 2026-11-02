# Program 4.3: Number Series Using For Loop

# Series 1: 1 se 10 tak simple ginti
print("--- Series 1: Numbers from 1 to 10 ---")
for i in range(1, 11):
    print(i, end=" ")
print()

# Series 2: Even numbers (2, 4, 6, 8, 10) -> step size = 2
print("\n--- Series 2: Even Numbers (2 to 10) ---")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Series 3: Reverse counting (10 se 1 tak) -> step size = -1
print("\n--- Series 3: Reverse Counting (10 to 1) ---")
for i in range(10, 0, -1):
    print(i, end=" ")
print()
