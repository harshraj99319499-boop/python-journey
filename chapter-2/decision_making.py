# Decision Making: if, elif, else

marks = 75

# Shart 1: Agar marks 80 ya usse zyada hain
if marks >= 80:
    print("Grade: A")

# Shart 2: Agar pehli galat hai, par marks 60 ya usse zyada hain
elif marks >= 60:
    print("Grade: B")

# Shart 3: Agar marks 40 ya usse zyada hain
elif marks >= 40:
    print("Grade: C")

# Aakhri rasta: Agar upar ka kuch bhi match na ho
else:
    print("Fail")
