"""
j = 3 # Ganzzahl
f = 3.5 # Dezimalzahl
tup = (3, 3.5, 4, 6, 2) # Tuple
lis = [3, 3.5, 4, 6, 2] # Liste

for el in tup:
    print(el)

if j > f:
    print("Ganzzahl ist kleiner")
elif j < f:
    print("Ganzzahl ist größer")
else:
    print("gleich groß")

b = True
b2 = False

if b and b2: # "&&" exisiert nicht, stattdessen "and"
    print("beides gleich")

for i in range(10 + 1):
    print(i)

for i in range(5, 10 + 1):
    print(i)

for i in range(5,10 + 1,2):
    print(i)
"""


# Beginn der Funktion
def addition(x, y):
    print(__name__)
    return x + y;


# Ende der Funktion

print(addition(3, 1))

if __name__ == "__nameUnknown__":
    print(addition(3, 1))
