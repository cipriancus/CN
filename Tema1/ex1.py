def ex1():
    u = 1.0
    while 1.0 + u != 1.0:
        aux = u #ultima valoare(cea mai mica) la care am avut inegalitatea
        u /= 10
    return aux

if(__name__=="__main__"):
    print(ex1())
