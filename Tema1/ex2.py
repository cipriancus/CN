import random

x = 1.0
u = 16
y = u
z = u

print('Asocitativitatea este')
print((x + y) + z == x + (y + z))

while (x * y) * z == x * (y * z):
    x = random.uniform(0, 1.0)
    y = random.uniform(0, 1.0)
    z = random.uniform(0, 1.0)

print(x, y, z)
