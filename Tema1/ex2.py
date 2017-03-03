import random
import ex1


def ex2():
    x = 1.0
    u = ex1.ex1()
    y = u
    z = u
    string_ret='Asocitativitatea este:'
    a=((x + y) + z == x + (y + z))
    string_ret=string_ret+' '+str(a)+'<br>'

    while (x * y) * z == x * (y * z):
        x = random.uniform(0, 1.0)
        y = random.uniform(0, 1.0)
        z = random.uniform(0, 1.0)
    string_ret=string_ret+'<br> Valori pentru care inmultirea nu este asociativa: '+'<br>'+str(x)+' '+str(y)+' '+str(z)
    return string_ret