n = int(input("Jep n: "))

if n > 0:
    rezultati = "Pozitiv"
elif n == 0:
    rezultati = "Zero"
else:
    rezultati = "Negativ"

if n % 5 == 0 and n != 0:
    rezultati += " (Sh.m i 5)"

print(rezultati)
