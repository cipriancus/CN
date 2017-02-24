import math
import random

c1=1.0/math.factorial(3)
c2=1.0/math.factorial(5)
c3=1.0/math.factorial(7)
c4=1.0/math.factorial(9)
c5=1.0/math.factorial(11)
c6=1.0/math.factorial(13)

random_no=list()

error1=list()
error2=list()
error3=list()
error4=list()
error5=list()
error6=list()


for iterator in range(0,10000):
    random_no.append(random.uniform(-math.pi/2,math.pi/2))
    x=random_no[iterator]

    y=pow(x,2)
    p1=x-c1*pow(x,3)+c2*pow(x,5)
    p2=p1-c3*pow(x,7)
    p3=p2+c4*pow(x,9)
    p4=x-0.166*pow(x,3)+0.00833*pow(x,5)-c3*pow(x,7)+c4*pow(x,9)
    p5=p4-c5*pow(x,11)
    p6=p5+c6*pow(x,13)

    error1.append(abs(p1-math.sin(x)))
    error2.append(abs(p2-math.sin(x)))
    error3.append(abs(p3-math.sin(x)))
    error4.append(abs(p4-math.sin(x)))
    error5.append(abs(p5-math.sin(x)))
    error6.append(abs(p6-math.sin(x)))

media1=0
media2=0
media4=0
media3=0
media5=0
media6=0

for iterator in range(0,10000):
    media1=(media1+error1[iterator])/2
    media2=(media1+error2[iterator])/2
    media3=(media1+error3[iterator])/2
    media4=(media1+error4[iterator])/2
    media5=(media1+error5[iterator])/2
    media6=(media1+error6[iterator])/2

print(media1,media2,media3,media4,media5,media6)
print(min(media1,media2,media3,media4,media5,media6))


    #p1=x*(1-c1*y+c2*pow(y,2))
    #p2=x*(1+y*(-c1+y*(c2-c3*y)))