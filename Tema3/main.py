from pip._vendor import colorama

epsilon = 10 ** -15


# de verificat ca o linie nu are mai mult de 10 elemente
def memorare_economica(nume_fis):
    print("Se memoreaza valorile din fisierul", nume_fis, ".")
    n = int(open(nume_fis).readline())
    d = [0.0 for i in range(n + 1)]
    val = [0.0 for i in range(n + 1)]
    col = [-i - 1 for i in range(n + 1)]
    b = list()
    ok = 0
    for line in open(nume_fis):
        if "," in line:
            elem, x, y = line.split(",")
            if float(x) == float(y):
                d[int(x)] = float(elem)
            else:
                col.insert(col.index(-int(x) - 1) + 1, float(y) + 1)
                val.insert(col.index(-int(x) - 1) + 1, float(elem))

        else:
            aux = line.strip("\n")
            if len(aux) > 1 and ok == 1:
                b.append(float(aux))
            ok = 1
    open("output_" + nume_fis, "wt").write(str(n) + "\n")
    open("output_" + nume_fis, "a").write(str(d) + "\n")
    open("output_" + nume_fis, "a").write(str(val) + "\n")
    open("output_" + nume_fis, "a").write(str(col) + "\n")
    open("output_" + nume_fis, "a").write(str(b) + "\n")


f = open("output_a.txt")
n_a = int(f.readline())
d_a = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
val_a = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
col_a = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
b_a = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]

f = open("output_b.txt")
n_b = int(f.readline())
d_b = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
val_b = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
col_b = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
b_b = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]

f = open("output_aorib.txt")
n_aorib = int(f.readline())
d_aorib = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
val_aorib = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
col_aorib = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
b_aorib = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]

f = open("output_aplusb.txt")
n_aplusb = int(f.readline())
d_aplusb = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
val_aplusb = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
col_aplusb = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
b_aplusb = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]

f = open("output_transpus_b.txt")
n_b_t = int(f.readline())
d_b_t = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
val_b_t = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
col_b_t = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
b_b_t = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]

x = [n_a - i + 1 for i in range(1, n_a + 1)]


def a_plus_b():
    print("\nSe calculeaza A+B si se verifica daca rezultatul\neste identic cu cel din fisier:")
    identical = True
    d = [0.0 for i in range(n_a + 1)]
    val = [0.0 for i in range(n_a + 1)]
    col = [-i - 1 for i in range(n_a + 1)]
    for elem_a, elem_b, elem_aplusb in zip(d_a, d_b, d_aplusb):
        d.append(elem_a + elem_b)
        if abs(elem_a + elem_b - elem_aplusb) > epsilon:
            identical = False
            print(1)
    x = -1
    while -x < n_a:
        lista_val = list()
        lista_col = list()
        line_a = col_a[col_a.index(x) + 1:col_a.index(x - 1)]
        line_b = col_b[col_b.index(x) + 1:col_b.index(x - 1)]
        line_aplusb = val_aplusb[col_aplusb.index(x) + 1:col_aplusb.index(x - 1)]
        for i in range(0, len(line_a)):
            lista_val.append(val_a[col_a.index(x) + 1 + i])
            lista_col.append(line_a[i])
        for i in range(0, len(line_b)):
            if line_b[i] in line_a:
                lista_val[line_a.index(line_b[i])] += val_b[col_b.index(x) + 1 + i]
            else:
                lista_col.append(line_b[i])
                lista_val.append(val_b[col_b.index(x) + 1 + i])
        for e, i in zip(lista_val, lista_col):
            val.insert(col.index(x) + 1, e)
            col.insert(col.index(x) + 1, i)
            if e not in line_aplusb:
                identical = False
                print(e)
        x -= 1
    print("\tCalculul pt A+B este corect:", identical)
    return d, val, col


def aorix(d, val, col, b, name):
    print("\nSe calculeaza " + name + "*x si se verifica daca rezultatul\neste identic cu cel din fisier:")
    iterator = -1
    b_aux = list()
    identical = True
    while -iterator < n_a:
        elem_b = d[-iterator - 1] * x[-iterator - 1]
        for index, elem in zip(col[col.index(iterator) + 1:col.index(iterator - 1)],
                               val[col.index(iterator) + 1:col.index(iterator - 1)]):
            elem_b += elem * x[int(index) - 1]
        b_aux.append(elem_b)
        if abs(b[-iterator - 1] - b_aux[-iterator - 1]) > epsilon:
            identical = False
            print(b[-iterator - 1], b_aux[-iterator - 1], -iterator - 1)
        iterator -= 1
    print("\tCalculul pt " + name + "*x este corect:", identical)
    return b_aux


def memorare_economica_transpus(nume_fis):
    print("Se memoreaza valorile din fisierul", nume_fis, ".")
    n = int(open(nume_fis).readline())
    d = [0.0 for i in range(n + 1)]
    val = [0.0 for i in range(n + 1)]
    col = [-i - 1 for i in range(n + 1)]
    b = list()
    ok = 0
    for line in open(nume_fis):
        if "," in line:
            elem, x, y = line.split(",")
            if float(x) == float(y):
                d[int(x)] = float(elem)
            else:
                col.insert(col.index(-int(y) - 1) + 1, float(x) + 1)
                val.insert(col.index(-int(y) - 1) + 1, float(elem))

        else:
            aux = line.strip("\n")
            if len(aux) > 1 and ok == 1:
                b.append(float(aux))
            ok = 1
    print(d)
    print(val)
    print(col)
    open("output_transpus_" + nume_fis, "wt").write(str(n) + "\n")
    open("output_transpus_" + nume_fis, "a").write(str(d) + "\n")
    open("output_transpus_" + nume_fis, "a").write(str(val) + "\n")
    open("output_transpus_" + nume_fis, "a").write(str(col) + "\n")
    open("output_transpus_" + nume_fis, "a").write(str(b) + "\n")


def aorib():
    print("\nSe calculeaza A*B si se verifica daca rezultatul\neste identic cu cel din fisier:")
    identical = True

    d = list()
    val = [0.0 for i in range(n_a + 1)]
    col = [-i - 1 for i in range(n_a + 1)]

    #linie in matricea rezultat; in loc de -10 ar tb sa fie -n_a
    for linie in range(-1, -10, -1):

        #calcul matrice
        print(linie)
        # element in matricea rezultat
        for coloana in range(-1,-n_a, -1):
            elem_sum = 0

            # linie din matricea A memorata economic
            for index_a, elem_a in zip(col_a[col_a.index(linie) + 1:col_a.index(linie - 1)],
                                       val_a[col_a.index(linie) + 1:col_a.index(linie - 1)]):

                try:
                    # unele elemente trebuie inmultite cu elemente de pe diaginala
                    if index_a == -coloana-1:
                        elem_sum += elem_a * d_b[-coloana-1]
                    else:
                        # pentru celelaltele, cautam elementul din linia lui B transpus de pe aceeasi coloana
                        index_b = index_a
                        elem_b = val_b_t[col_b_t[col_b_t.index(coloana) + 1:col_b_t.index(coloana - 1)].index(index_b)]
                        if index_b == -linie-1:
                            elem_sum += elem_b * d_a[-linie-1]
                        else:
                            elem_sum += elem_b * elem_a
                except Exception as e:
                    pass
            # acest if functioneaza, diagonala e calculata corect
            if linie == coloana:
                elem_sum += d_a[-linie - 1] * d_b[-coloana - 1]
                d.append(elem_sum)
                if abs(d[-linie - 1] - d_aorib[-linie - 1]) > epsilon:
                    identical = False
            # acest else nu ar trebui sa afecteze rezultatul
            else:
                if elem_sum > epsilon:
                    col.insert(col.index(linie) + 1, -coloana)
                    val.insert(col.index(linie) + 1, elem_sum)
    # cand le afisez, nu au elemente comune de la -1 pana la -2
    print(val)
    print(val_aorib)
    print(col)
    print(col_aorib)


# decomenteaza pt a calcula
# o fi ea memorare economica de spatiu, dar nu e economica de timp

# memorare_economica("a.txt")
# memorare_economica("b.txt")
# memorare_economica("aorib.txt")
# memorare_economica("aplusb.txt")
# memorare_economica_transpus("b.txt")

# a_plus_b()
# aorix(d_a, val_a, col_a, b_a, "A")
# aorix(d_b, val_b, col_b, b_b, "B")

aorib()
