import copy
import time
import numpy

epsilon = 10 ** -15

# n = int(input('insert n dimension'))
# a = [[0 for x in range(n)] for y in range(n)]
#
# print('Dati elementele matricii:')
# for iterator in range(0, n):
#     for iterator2 in range(0, n):
#         a[iterator][iterator2] = float(input())

def calc_a1(a, n):
    max = a[0][0]
    for iterator in range(0, n):
        sum = 0
        for iterator2 in range(0, n):
            sum = sum + a[iterator][iterator2]

        if max < sum:
            max = sum
    return max


def calc_inf(a, n):
    max = a[0][0]
    for iterator in range(0, n):
        sum = 0
        for iterator2 in range(0, n):
            sum = sum + a[iterator2][iterator]

        if max < sum:
            max = sum
    return max

def initializare(a, n):
    At = numpy.transpose(numpy.matrix(a)).tolist()
    a1 = calc_a1(a, n)
    ainf = calc_inf(a, n)
    for iterator in range(0, n):
        for iterator2 in range(0, n):
            At[iterator][iterator2] = At[iterator][iterator2] / (a1 * ainf)
    return At

def metoda1(V1, n, a):
    BV = numpy.dot(numpy.dot(-1,numpy.matrix(a)), numpy.matrix(V1))#-AV

    BV=BV.tolist()
    for iterator in range(0,n):
        BV[iterator][iterator]=BV[iterator][iterator]+2
    BV=numpy.matrix(BV)

    vk1 = numpy.dot(V1, BV)
    return vk1.tolist()

def metoda2(V1, n, a):
    C = numpy.dot(numpy.dot(-1,numpy.matrix(a)), numpy.matrix(V1))
    BV = C.tolist()
    for iterator in range(0, n):
        BV[iterator][iterator] = BV[iterator][iterator] + 3
    BV = numpy.matrix(BV)

    C=numpy.dot(C,BV)
    C = C.tolist()
    for iterator in range(0, n):
        C[iterator][iterator] = C[iterator][iterator] + 3
    C = numpy.matrix(C)

    C = numpy.dot(C,V1)
    return C.tolist()

def metoda3(V1, n, a):
    BV = numpy.dot(numpy.dot(-1,numpy.matrix(a)), numpy.matrix(V1))#-AV

    patrat=BV.tolist()
    for iterator in range(0, n):
        patrat[iterator][iterator] = patrat[iterator][iterator] + 3
    patrat = numpy.matrix(patrat)
    patrat=numpy.dot(numpy.matrix(patrat),numpy.matrix(patrat))

    BV=BV.tolist()
    for iterator in range(0, n):
        BV[iterator][iterator] = BV[iterator][iterator] + 1

    patrat=numpy.dot(float(1/4),numpy.dot(numpy.matrix(BV),numpy.matrix(patrat)))

    patrat = patrat.tolist()
    for iterator in range(0, n):
        patrat[iterator][iterator] = patrat[iterator][iterator] + 1

    patrat=numpy.dot(numpy.matrix(patrat),numpy.matrix(V1))
    return patrat.tolist()

n = 3
a = [[7,8,9],[17,2,3],[5,4,3]]


def invers(a,n,metoda):
    epsilon = 10 ** -15
    kmax = 10000
    k = 0
    dv = 1

    V0 = V1 = initializare(a, n)

    while dv >= epsilon and k <= kmax and dv <= pow(10, 8):
        V0 = copy.copy(V1)
        if metoda==1:
            V1 = metoda1(V1, n, a)
        elif metoda==2:
            V1 = metoda2(V1, n, a)
        else:
            V1 = metoda3(V1, n, a)
        dv = numpy.linalg.norm(numpy.subtract(numpy.matrix(V0),numpy.matrix(V1)))
        k = k + 1

    if dv < epsilon:
        return (k,V1)
    else:
        print('Divergenta')
        return (0,0)

start = time.time()
(k,inv)=invers(a,n,1)
if k != 0:
    print(inv)
    end = time.time()
    print("Timpul de calcul pentru metoda 1 este " + str(end - start))
    print("Numarul de iteratii este " + str(k))
    print('Norma este '+str(numpy.linalg.norm(numpy.subtract(numpy.dot(numpy.matrix(a),numpy.matrix(inv)),numpy.identity(n)))))
    print('\n')

start = time.time()
(k,inv)=invers(a,n,2)
if k != 0:
    print(inv)
    end = time.time()
    print("Timpul de calcul pentru metoda 2 este " + str(end - start))
    print("Numarul de iteratii este " + str(k))
    print('Norma este '+str(numpy.linalg.norm(numpy.subtract(numpy.dot(numpy.matrix(a),numpy.matrix(inv)),numpy.identity(n)))))
    print('\n')
#
# (-2)^0 (-2)^1 (-2)^2 ...
#   0    (-2)^0  ...
#   ...
#   ...
#   ................(-2)^0

a=[[1,2,0],[0,1,2],[0,0,1]]

start = time.time()
(k,inv)=invers(a,n,3)
if k != 0:
    print(inv)
    end = time.time()
    print("Timpul de calcul pentru metoda 3 este " + str(end - start))
    print("Numarul de iteratii este " + str(k))
    print('Norma este '+str(numpy.linalg.norm(numpy.subtract(numpy.dot(numpy.matrix(a),numpy.matrix(inv)),numpy.identity(n)))))

def afisare_matrice(matrix,fisier,n):
    for iterator in range(0,n):
        for iterator2 in range(0,n):
            fisier.write(' '+str(matrix[iterator][iterator2]))
        fisier.write('\n')
    fisier.write('\n')

def shift_matrice(matrix,n):
    n=n-1
    matrix[0].append(0)
    for iterator in range(1,n):
        matrix[iterator]=[0]+matrix[iterator-1]
        matrix[iterator].pop()

    matrix.append([0]+matrix[n-1])
    matrix[n].pop()


fisier=open("matrice.txt",mode="wt")
numar_afisari=10
n=3
base_matrix=[[1,2,0],[0,1,2],[0,0,2]]

for iterator in range(0,numar_afisari):
    (k,inv)=invers(base_matrix,n,1)

    afisare_matrice(inv,fisier,n)
    n=n+1
    shift_matrice(base_matrix,n)