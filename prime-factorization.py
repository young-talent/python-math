from time import time
from math import floor

while True:
    zahl = int(input("Zahl, die Primfaktorzerlegt werden soll: "))
    start = time()

    while zahl > 1:
        i = 2

        while floor(zahl / i) != (zahl / i):
            i = i + 1

        print(i, end="; ")
        zahl = zahl / i
    print("\n", "Die Berechnungen haben ", round(time() - start, 3), "s gedauert.", sep="", end="\n\n")
