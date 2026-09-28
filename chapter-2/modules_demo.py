# 1. import: Pura module load karna
import math

print("Square root of 16:", math.sqrt(16))


# 2. from: Module me se sirf ek specific tool nikalna
from math import pi

print("Value of PI:", pi)


# 3. as: Kisi module ya tool ko chhota nickname dena
import math as m

# Ab 'math.floor' ki jagah 'm.floor' use kar sakte hain
print("Floor value of 4.9:", m.floor(4.9))
