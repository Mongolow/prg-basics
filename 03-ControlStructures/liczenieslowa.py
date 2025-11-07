a = str(input('podaj slowo '))
b = 0

for char in a:
    if char == 'b':
        b = b + 1
    else:
        continue


print(b)