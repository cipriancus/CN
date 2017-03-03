from itertools import count
import copy

a = [[1, -1, 2],
     [-1, 5, -4],
     [2, -4, 6]]

copyOfA=copy.deepcopy(a)

b = [1, 0, 1]

d = [0, 0, 0]

n = 3

eps = 10 ** -10

# factorizare Choleski
for p in range(n):
    s = 0
    for k in range(p):
        s += d[k] * a[p][k] * a[p][k]
    d[p] = a[p][p] - s
    for i in range(p + 1, n):
        s = 0
        for k in range(p):
            s += (d[k] * a[p][k] * a[i][k])
        if abs(d[p]) > eps:
            a[i][p] = (a[i][p] - s) / d[p]
        else:
            print("Nu se poate face impartirea.")
    for i in range(p + 1):
        a[i][p] = 0

print("D este:", d)
print("L este:", a)

# determinantul lui A
detA = 1
for i in range(n):
    detA *= d[i]

print("det(A) este:", detA)

# x chol
# y = D Lt x din Lx = b
y = [None] * n
for i in range(n):
    y[i] = b[i]
    for j in range(i):
        if (i > 0):
            y[i] -= a[i][j] * y[j]

# z = Lt x din Dz = y
z = [None] * n
for i in range(n):
    z[i] = y[i]
    if abs(d[i]) > eps:
        z[i] /= d[i]
    else:
        print("Nu se poate face impartirea.")

# aflare x din Ltx = z
x = [None] * n
for i in range(n - 1, -1, -1):
    x[i] = z[i]
    for j in range(n - 1, i, -1):
        if i < n - 1:
            x[i] -= a[j][i] * x[j]

print("x Chol este:", x)

# verificat matricea sa fie sim si poz(nu stiu exact daca e necesar)
# aceleasi calcule folosind o biblioteca
# verificarea solutiei prin calcularea normei

# citit de la tastatuta conform problemei
#   (mai bine sa o faci la sfarsit ca sa nu trebuiasca sa tot
#    introduci date cand testezi)

#-----------------------LDLT cu numpy----------------------------------
import numpy
print('-------------------------LIBRARIA------------------------')

A=numpy.array(copyOfA)
L=numpy.linalg.cholesky(A)#descompunerea LLT

#Pentru a forma LDLT din LLT
#folosim un S care are diagonala din L

S=numpy.zeros((n,n))

for i in range(0,n):#parcurgem diag L
    S[i][i]=L[i][i]

D=numpy.dot(S,S)#D=S^2
L=numpy.dot(L,numpy.linalg.inv(S))#L=L*S^-1

print('D este',D)
print('L este',L)
print('Inmultirea da ',numpy.dot(numpy.dot(L,D),L.T.conj()))

#----------------------DESCOMPUNEREA LU-----------------------

A=numpy.array(copyOfA)
L=numpy.linalg.cholesky(A)
print('Descompunerea LU cu L: ',L)#descompunerea LU, daca A e sim si poz definita

#-------------------------Solutia sistemului -----------------
x=numpy.linalg.solve(A,b)
print('Solutia librariei pentru sistem este: ',x)

#-------------------------Norma-------------------------------
A=numpy.subtract(numpy.dot(A,x),b)#A*x-b
print('Norma este: ',numpy.linalg.norm(A,ord=2))#calc norma 2, sqrt(sum(abs(xi)^2))
