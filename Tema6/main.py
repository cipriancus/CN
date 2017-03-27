import math
import random
import time
import numpy as np

p = 504
n = 502
epsilon = 10 ** -9
kmax = 1000000


def generare_a(n):
    # cautat matrice rara
    m = random.randint(100, int(n * n / 1000))
    open("a.txt", "wt").write(str(n) + "\n\n")
    for i in range(0, m):
        x = str(int(random.random() * 502))
        y = str(int(random.random() * 502))
        elem = str(random.random() * (-1) ** random.randint(1, 10))
        open("a.txt", "a").write(elem + "," + x + "," + y + "\n")
        open("a.txt", "a").write(elem + "," + y + "," + x + "\n")
    for i in range(0, n):
        if (-1) ** random.randint(1, 10) > 0:
            elem = str(random.random() * 1000 * (-1) ** random.randint(1, 10))
            open("a.txt", "a").write(elem + "," + str(i) + "," + str(i) + "\n")


# verificare matrice simetrica din fisier
vaux = dict()
caux = dict()
aux = dict()


def memorare_economica(nume_fis):
    global aux
    aux = dict()
    n = int(open(nume_fis).readline())
    d = [0 for i in range(n + 1)]
    val = list()
    col = list()

    for line in open(nume_fis):
        if "," in line:
            line = line[:-1]
            elem, x, y = line.split(",")
            aux[(x, y)] = elem
            if float(x) == float(y):
                d[int(x)] = float(elem)
            else:
                if -int(x) - 1 in vaux:
                    caux[-int(x) - 1].append(float(y) + 1)
                    vaux[-int(x) - 1].append(float(elem))
                else:
                    vaux[-int(x) - 1] = list()
                    caux[-int(x) - 1] = list()
                    caux[-int(x) - 1].append(float(y) + 1)
                    vaux[-int(x) - 1].append(float(elem))

    for i in range(-1, -n - 1, -1):
        val += [0]
        col += [i]
        if i in vaux:
            val += vaux[i]
            col += caux[i]
    val += [0]
    col += [-n - 1]
    return n, d, val, col


def verificare_simetrica():
    for (x, y), v in aux.items():
        if (y, x) not in aux:
            print("first if")
            return False
        elif float(v) - float(aux[(y, x)]) > epsilon:
            print(v, aux[(y, x)])
            print("second if")
            return False
    return True


print("Generare matrice patratica, rara, simetrica.")
# generare_a(n)
print("Memorare economica matricea generata.")
n_a, d_a, val_a, col_a = memorare_economica("a.txt")
print("Memorare economica matricea din fisier.")
n_m, d_m, val_m, col_m = memorare_economica("m_rar_sim_2017.txt")
print("Verificarea ca matricea din fisier este simetrica intoarce",verificare_simetrica())


def norma_euclidiana(vector):
    norma = 0
    for elem in vector:
        norma += elem * elem
    return math.sqrt(norma)


def norma_infinit(matrice):
    max = 0
    for i in range(p):
        sum = 0
        for j in range(n):
            sum += abs(matrice.item(i, j))
        if sum > max:
            max = sum
    return max


def suma_patrate(vector):
    norma = 0
    for elem in vector:
        norma += elem * elem
    return norma


def v_0(n):
    v = list()
    for i in range(0, n):
        v.append(random.random())
    v = inm_scalar(v, 1 / norma_euclidiana(v))
    return v


def aorix(x, n, d, val, col, name):
    b_aux = [0 for i in range(n)]
    elem_b = 0

    for elem, index in zip(val, col):
        index = int(index)
        if index < 0:
            if -1 < -index - 1 < n:
                b_aux[-index-2] = elem_b
                elem_b = d[-index - 1] * x[-index - 1]
        else:
            elem_b += elem * x[index - 1]

    return b_aux


def inm_scalar(vector, scalar):
    for i in range(0, len(vector)):
        vector[i] *= scalar
    return vector


def diferenta(w, l0, v0):
    dif = list()
    v0 = inm_scalar(v0, l0)
    for elem_w, elem_v in zip(w, v0):
        dif.append(elem_w - elem_v)
    return dif


def diferenta_mat(a, b, n, p):
    for i in range(n):
        for j in range(p):
            a[i][j] = a.item(i, j) - b.item(i, j)
            return a


def produs_scalar(w, v0):
    l0 = 0
    for elem1, elem2 in zip(w, v0):
        l0 += elem1 * elem2
    return l0


def metoda_puterii(n, d, val, col):
    v0 = v_0(n)
    w = aorix(v0, n, d, val, col, "A")
    l0 = produs_scalar(w, v0)
    k = 0

    while norma_euclidiana(diferenta(w, l0, v0)) > n * epsilon and k <= kmax:
        v0 = inm_scalar(w, 1 / norma_euclidiana(w))
        w = aorix(v0, n, d, val, col, "A")
        l0 = produs_scalar(w, v0)
        k += 1
    else:
        v0 = inm_scalar(w, 1 / norma_euclidiana(w))
        w = aorix(v0, n, d, val, col, "A")
        l0 = produs_scalar(w, v0)
        k += 1

    if k == kmax:
        print("nu a convers")
    else:
        print("Cea mai mare valoare proprie", l0)
        print("Valori proprii", v0, "\n\n")

print("Metoda puterii pt matricea din fisier:")
metoda_puterii(n_m, d_m, val_m, col_m)
print("Metoda puterii pt matricea generata:")
metoda_puterii(n_a, d_a, val_a, col_a)


def generare_clasic(n, p, m):
    a = ""
    for i in range(p):
        for j in range(n):
            if m == 0:
                elem = str(random.random() * (-1) ** random.randint(1, 10))
            else:
                elem = m[i][j]
            a += str(elem) + " "
        a += ";"
    a = a[:-1]
    a = np.matrix(a)
    return a


n = 2
p = 3
a = [[2, 7], [5, 3], [4, 1]]
a = generare_clasic(n, p, a)
u, s, v = np.linalg.svd(a)
print("Valori proprii", s)

rang = 0
for elem in s:
    if elem > 0:
        rang += 1
print("rang", rang)
print("Nr de conditionare", max(s) / min(s))

S = np.zeros((p, n))
S[:n, :n] = np.diag(s)
v = v.transpose()
s = np.dot(u, np.dot(S, v))
print("Norma infinit: ", norma_infinit(diferenta_mat(a, s, n, p)))


def calc_As(s):
    a = [[0.0 for i in range(n)] for j in range(p)]
    for k in range(s):
        for i in range(p):
            for j in range(n):
                a[i][j] += S.item(k, k) * u.item(k, i) * v.item(k, j)
    As = ""
    for i in range(p):
        for j in range(n):
            As += str(a[i][j]) + " "
        As += ";"
    As = As[:-1]
    As = np.matrix(As)
    return As


s = input("Dati s:")
As = calc_As(int(s))

print("Norma infinit: ", norma_infinit(diferenta_mat(a, As, n, p)))
