import random

def heitäNoppaa(tahkot):
    luku = random.randint(1, tahkot)
    return luku


tahkoLKM = int(input("Kuinka monta tahkoa? "))
while True:
    silmäLuku = heitäNoppaa(tahkoLKM)
    print(silmäLuku)
    if silmäLuku == tahkoLKM:
        break