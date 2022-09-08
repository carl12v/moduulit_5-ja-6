from math import *

def main():
    dia = eval(input("Kirjoita pizzan koko: "))
    cost = eval(input("Kirjoita pizzan hinta: "))
    r = dia / 2
    area = (pi * r**2)
    print("Pizzan hinta on", round(cost/area, 2), "euroa")

main()