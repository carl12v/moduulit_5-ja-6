while True:
    try:
        kaupunki1 = (input("Kirjoita kaupunki: "))
        kaupunki2 = (input("Kirjoita kaupunki: "))
        kaupunki3 = (input("Kirjoita kaupunki: "))
        kaupunki4 = (input("Kirjoita kaupunki: "))
        kaupunki5 = (input("Kirjoita kaupunki: "))
    except ValueError:
        print("Tämä ei kelpaa.")
        continue
    else:
        break
print(f"kaupunki {kaupunki1}")
print(f"kaupunki {kaupunki2}")
print(f"kaupunki {kaupunki3}")
print(f"kaupunki {kaupunki4}")
print(f"kaupunki {kaupunki5}")