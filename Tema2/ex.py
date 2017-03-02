a = [[1, -1, 2],
     [-1, 5, -4],
     [2, -4, 6]]

d = [0, 0, 0]

l = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

lt = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

n = 3
for p in range(n):
    s = 0
    for k in range(p):
        s += d[k] * l[p][k] * l[p][k]
    d[p] = a[p][p] - s
    for i in range(p + 1, n):
        s = 0
        for k in range(p):
            s += (d[k] * l[p][k] * l[i][k])
        l[i][p] = (a[i][p] - s) / d[p]

print(d)
print(l)

for i in range(n):
    for j in range(n):
        lt[i][j] = l[j][i]

print(lt)

detA = 1
for i in range(n):
    detA *= d[i]

print(detA)