import random
linijka = []

for y in range (1,20):
    for x in range(1,8):
        liczba = random.randint(1,49)
        linijka.append(liczba)
    print(*linijka)
    linijka = []
    



