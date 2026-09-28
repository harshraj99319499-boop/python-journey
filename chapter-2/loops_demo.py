# 1. for loop: 1 se lekar 5 tak number print karna
print("--- for loop ---")
for i in [1, 2, 3, 4, 5]:
    print(i)


# 2. while loop: Jab tak number 3 se chhota hai tab tak chalega
print("\n--- while loop ---")
count = 1
while count <= 3:
    print(count)
    count = count + 1


# 3. break: Agar number 3 aaye toh loop wahin rok do
print("\n--- break ---")
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break  # Yahan loop band ho jayega
    print(i)


# 4. continue: Agar number 3 aaye toh use chhod do, aage badho
print("\n--- continue ---")
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        continue  # 3 print nahi hoga, seedha 4 par jayega
    print(i)


# 5. pass: Jab abhi kuch nahi karna ho (khali jagah)
print("\n--- pass ---")
for i in [1, 2]:
    pass  # Kuch nahi karega, error bhi nahi dega
print("Pass executed successfully!")
