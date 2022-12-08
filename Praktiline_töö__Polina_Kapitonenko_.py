8. 
from math import*
print("Kütusekulu arvitamine")








1.
print("Puu läbimõõdu arvumine")
C=float(input("Puu ümbermõõt: "))
d=2(C/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")


from math import *
from random import *

2.
print("Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus=> "))
M=float(input("Sisesta ristküliku 2. külje pikkus=> "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on m**2")


3.

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg/teepikkus
print()
print("Sinu kiirus oli " + str(kiirus) + " km/h")

4.
A1=int(input("Sisesta 1. arv => "))
A2=int(input("Sisesta 2 arv => "))
A3=int(input("Sisesta 3. arv => "))
A4=int(input("Sisesta 4. arv => "))
A5=int(input("Sisesta 5. arv => "))
Keskmine=(A1+A2+A3+A4+A5)/5
print(f"Keskmine on {Keskmine}")


6.
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}")
print(f"Kolmnurga ümbermõõt = {a+b+c}")
print()

7.
from math import *
print("Pitsa Võtsite 3 sõbraga suure pitsa hinnaga 12,90€ te jätate tenindaja")
s=10*12,90/100
s=round(s)
d=(12,90+s)
print(f"Vastus: {d}")
p=d/3
p=round(p,1)
print (str(f"Iga sõber peab maksma: {p}€"))
print()



