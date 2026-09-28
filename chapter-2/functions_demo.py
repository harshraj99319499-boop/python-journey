# 1. def aur return (Normal Function)
# Ek function banaya jo do numbers ko jodta hai
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 10)
print("Function Output:", total)


# 2. lambda (Ek line ka chhota function)
# Ek number ka double nikalna
double = lambda x: x * 2

print("Lambda Output:", double(7))


# 3. class (Ek simple blueprint)
class Student:
    name = "Harsh"

# Class se ek object banaya
s1 = Student()
print("Class Student Name:", s1.name)
