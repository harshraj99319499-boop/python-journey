# 1. 'and' -> Dono shart sahi honi chahiye
print("--- 'and' operator ---")
print(10 > 5 and 20 > 10)   # Dono sahi -> True
print(10 > 5 and 20 < 10)   # Ek galat ho gaya -> False


# 2. 'or' -> Koi ek bhi sahi ho toh chalega
print("\n--- 'or' operator ---")
print(10 > 5 or 20 < 10)    # Pehla sahi hai -> True
print(10 < 5 or 20 < 10)    # Dono hi galat hain -> False


# 3. 'not' -> Jawab ko ulta kar deta hai
print("\n--- 'not' operator ---")
sahi_baat = True
print(not sahi_baat)        # True ka ulta -> False

print(not (10 < 5))         # 10 < 5 galat tha, not ne True bana diya
