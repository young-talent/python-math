import time
import math
number = int(input("Alle Primzahlen von 0 bis "))
start_time = time.time()
if number > 1 :
	prime_numbers = [2]
	i = 1
	while i < number :
		i = i + 2
		n = 2
		while n ** 2 < i or not math.floor(i / n) = i / n :
			n = n + 1
		if not n ** 2 < i :
			prime_numbers.append(i)
	print(prime_numbers, "es hat", time.time() - start_time, "s gedauert")
else :
	print("Zu kleine Zahl!")
