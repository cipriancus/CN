import copy
import time
import numpy

epsilon = 10 ** -15


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
    In = numpy.dot(2, numpy.identity(n))
    av = numpy.dot(numpy.matrix(a), numpy.matrix(V1))
    diff = numpy.subtract(In, av)
    vk1 = numpy.dot(V1, diff)
    return vk1.tolist()

def metoda2(V1, n, a):
    In = numpy.dot(3, numpy.identity(n))
    av = numpy.dot(numpy.matrix(a), numpy.matrix(V1))
    diff = numpy.subtract(In, av)
    vk1 = numpy.dot(V1, diff)
    vk1 = numpy.dot(V1, numpy.subtract(In, numpy.dot(av, diff)))
    return vk1.tolist()

def metoda3(V1, n, a):
    In = numpy.dot(3, numpy.identity(n))
    av = numpy.dot(numpy.matrix(a), numpy.matrix(V1))

    av2=numpy.dot(numpy.subtract(In,av),numpy.subtract(In,av))
    vk=numpy.add(numpy.identity(n),numpy.dot(float(1/4),av2))
    return vk.tolist()

# n = int(input('insert n dimension'))
# a = [[0 for x in range(n)] for y in range(n)]
#
# print('Dati elementele matricii:')
# for iterator in range(0, n):
#     for iterator2 in range(0, n):
#         a[iterator][iterator2] = float(input())

n = 3
a = [[1,2,0],[0,1,2],[0,0,1]]

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

start = time.time()
(k,inv)=invers(a,n,1)
print(inv)
end = time.time()
print("Timpul de calcul pentru metoda 1 este " + str(end - start))
print("Numarul de iteratii este " + str(k))
print('Norma este '+str(numpy.linalg.norm(numpy.subtract(numpy.dot(numpy.matrix(a),numpy.matrix(inv)),numpy.identity(n)))))
print('\n')

start = time.time()
(k,inv)=invers(a,n,2)
print(inv)
end = time.time()
print("Timpul de calcul pentru metoda 2 este " + str(end - start))
print("Numarul de iteratii este " + str(k))
print('Norma este '+str(numpy.linalg.norm(numpy.subtract(numpy.dot(numpy.matrix(a),numpy.matrix(inv)),numpy.identity(n)))))
print('\n')

start = time.time()
(k,inv)=invers(a,n,3)
print(inv)
end = time.time()
print("Timpul de calcul pentru metoda 3 este " + str(end - start))
print("Numarul de iteratii este " + str(k))
print('Norma este '+str(numpy.linalg.norm(numpy.subtract(numpy.dot(numpy.matrix(a),numpy.matrix(inv)),numpy.identity(n)))))
