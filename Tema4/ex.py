import copy
import time

epsilon = 10 ** -8

start=time.time()

def search(ai, aicol, j):
    try:
        return ai[aicol.index(j)]
    except:
        return 0

def create_dictionary(val,col,n):
    positions=dict()
    for iterator in range(0,len(col)):
        if int(col[iterator])<0:
            positions[int(col[iterator])]=int(iterator)
    return positions

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

                # verificam daca nu exista elementa nule in diagonala
                if abs(float(elem)) < epsilon:
                    print("Matricea are elemente nule")
                    exit(1)
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


# memorare_economica("m_rar_2017_1.txt")
# memorare_economica("m_rar_2017_2.txt")
# memorare_economica("m_rar_2017_3.txt")
# memorare_economica("m_rar_2017_4.txt")

fisier = "output_m_rar_2017_4.txt"

f = open(fisier)
n = int(f.readline())
d = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
val = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
col = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]
b = [float(e) for e in f.readline().strip("[").strip("]\n").split(", ")]

# era un mic bug, baga 0.0 la final
if len(d) > n:
    d.pop()
positions=create_dictionary(val,col,n)

#verificam asigurarea convergentei
convergenta=True
for iterator in range(0,n):
    element=abs(d[iterator])#elementul |aii|

    #selectam linia i
    linie=val[positions[-iterator-1] + 1:positions[-iterator - 2]]
    sum=0
    for iterator2 in linie:
        sum=sum+abs(iterator2)

    if element < sum:
        convergenta=False
        print("Convergenta nu este asigurata")
        break

if convergenta == True:
    print("Matricea este convergenta")


kmax = 10000
k = 0
xk = [0 for i in range(0, n)]
dx = 0

xkcopy = copy.deepcopy(xk)


# calc noul xk, cu i de la 0,n-1
for iterator in range(0,n):
    try:
        ai = val[positions[-iterator - 1] + 1:positions[-iterator - 2]]  # iau linia ai ca sa o folosesc peste tot
        aicol = col[positions[-iterator - 1]  + 1:positions[-iterator - 2]]  # iau si coloanna ca sa stiu unde sunt

        q = 0  # suma de la j=1 la i-1 aij xj k+1
        p = 0  # suma de la i+1 la n din aij xj k

        for coloana in aicol:
            if coloana >= 1 and coloana <= iterator:
                q = q + search(ai, aicol, int(coloana)) * xk[int(coloana)]  # xj
            elif coloana >= iterator + 1 and coloana < n:
                p = p + search(ai, aicol, int(coloana)) * xkcopy[int(coloana)]
        xk[iterator] = (b[iterator] - q - p) / d[iterator]
    except Exception as e:
        print(e)
        pass

# dx=||xk-xcopy||
dx = float(0)
for iterator in range(0, n):
    dx = dx + abs(xk[iterator] - xkcopy[iterator])
print(xk[0])
k = k + 1

while dx >= epsilon and k <= kmax and dx <= pow(10, 8):
    xkcopy = copy.deepcopy(xk)

    # calc noul xk, cu i de la 0,n-1
    for iterator in range(0, n):
        try:
            ai = val[positions[-iterator - 1] + 1:positions[-iterator - 2]]  # iau linia ai ca sa o folosesc peste tot
            aicol = col[positions[-iterator - 1] + 1:positions[-iterator - 2]]  # iau si coloanna ca sa stiu unde sunt

            q = 0  # suma de la j=1 la i-1 aij xj k+1
            p = 0  # suma de la i+1 la n din aij xj k

            for coloana in aicol:
                if coloana >= 1 and coloana <= iterator:
                    q = q + search(ai, aicol, int(coloana)) * xk[int(coloana)]  # xj
                elif coloana >= iterator + 1 and coloana < n:
                    p = p + search(ai, aicol, int(coloana)) * xkcopy[int(coloana)]

            xk[iterator] = (b[iterator] - q - p) / d[iterator]
        except Exception as e:
            print(e)
            pass

    # dx=||xk-xcopy||
    dx = float(0)
    for iterator in range(0, n):
        dx = dx + abs(xk[iterator] - xkcopy[iterator])
    print(xk[0:3])
    k = k + 1


end=time.time()
print("Timpul de calcul este "+str(end-start))

print("Numarul de iteratii este "+str(k))

