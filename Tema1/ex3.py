import random
import math
import time
from ex2 import ex2
from ex1 import ex1
from flask import request
from flask import Flask, jsonify
import urllib
import json

app = Flask(__name__)

@app.route('/exercitiul1')
def call1():
    return str(ex1())

@app.route('/exercitiul2')
def call2():
    return ex2()


@app.route('/exercitiul3')
def ex3():
    fact = 2 * 3
    c1 = 1.0 / fact
    fact *= 4 * 5
    c2 = 1.0 / fact
    fact *= 6 * 7
    c3 = 1.0 / fact
    fact *= 8 * 9
    c4 = 1.0 / fact
    fact *= 10 * 11
    c5 = 1.0 / fact
    fact *= 12 * 13
    c6 = 1.0 / fact

    # suma erorilor pt fiecare polinom
    s1, s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0, 0
    # timpul de calcul pt fiecare polinom
    t1, t2, t3, t4, t5, t6 = 0, 0, 0, 0, 0, 0
    for i in range(10000):
        x = random.uniform(-math.pi, math.pi)
        y = x * x

        t = time.time()
        p1 = x * (1 + y * (-c1 + y * c2))
        t1 += time.time() - t
        # se adauga la suma diferenta in modul dintre functia sinus si valoarea polinomului
        s1 += (abs(p1 - math.sin(x)))

        t = time.time()
        p2 = x * (1 + y * (-c1 + y * (c2 - y * c3)))
        t2 += time.time() - t
        s2 += (abs(p2 - math.sin(x)))

        t = time.time()
        p3 = x * (1 + y * (-c1 + y * (c2 + y * (-c3 + y * c4))))
        t3 += time.time() - t
        s3 += (abs(p3 - math.sin(x)))

        t = time.time()
        p4 = x * (1 + y * (-0.166 + y * (0.00833 + y * (-c3 + y * c4))))
        t4 += time.time() - t
        s4 += (abs(p4 - math.sin(x)))

        t = time.time()
        p5 = x * (1 + y * (-c1 + y * (c2 + y * (-c3 + y * (c4 - y * c5)))))
        t5 += time.time() - t
        s5 += (abs(p5 - math.sin(x)))

        t = time.time()
        p6 = x * (1 + y * (-c1 + y * (c2 + y * (-c3 + y * (c4 + y * (-c5 + c6))))))
        t6 += time.time() - t
        s6 += (abs(p6 - math.sin(x)))

    a = {"Polimonul 1": s1, "Polimonul 2": s2, "Polimonul 3": s3, "Polimonul 4": s4, "Polimonul 5": s5,
         "Polimonul 6": s6}
    a = sorted(a.items(), key=lambda elem: elem[1])

    afisare=str()

    j = 0
    afisare=afisare + "Primele 3 polinoame cu cele mai mici erori "
    for i in a:
        if j < 3:
            afisare=afisare+' '+str(i)
            j += 1
        else:
            break

    afisare=afisare+'<br>'+"Ierarhia celor 6 polinoame:"

    for i in a:
        afisare=afisare+' '+i[0]

    afisare=afisare+'<br>'+"Timpul de calcul pt fiecare polinom: "

    afisare=afisare+"t1:"+str(t1)+' '
    afisare=afisare+"t2:"+str(t2)+' '
    afisare=afisare+"t3:"+str(t3)+' '
    afisare=afisare+"t4:"+str(t4)+' '
    afisare=afisare+"t5:"+str(t5)+' '
    afisare=afisare+"t6:"+str(t6)+' '

    return afisare

if __name__ == '__main__':
    app.run(threaded=True)
