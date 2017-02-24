import random
import ex1

x = 1.0
u = ex1.ex1()
y = u
z = u

print('Asocitativitatea este:')
print((x + y) + z == x + (y + z))

while (x * y) * z == x * (y * z):
    x = random.uniform(0, 1.0)
    y = random.uniform(0, 1.0)
    z = random.uniform(0, 1.0)
print("Valori pt care inmultirea nu este asociativa: ")
print(x, y, z)
