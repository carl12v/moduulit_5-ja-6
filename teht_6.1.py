import random

def heitäNoppaa():
    luku = random.randint(1, 6)
    return luku

while True:
    silmäLuku = heitäNoppaa()
    print(silmäLuku)
    if silmäLuku == 6:
        break