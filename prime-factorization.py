# Primfaktorzerlegung v1.0
import math, time

while(True):
    zahl = int(input("Zahl, die Primfaktorzerlegt werden soll: "))
    start = time.time()
    while(zahl > 1):
        i = 2
        while(math.floor(zahl / i) != (zahl / i)):
            i = i + 1
        print(i, end="; ")
        zahl = zahl / i
    print("\n", "Die Berechnungen haben ", round(time.time() - start, 3), "s gedauert.", sep="", end="\n\n")
