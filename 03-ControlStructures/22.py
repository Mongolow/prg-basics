string = ''

for x in range(1,31):
    if x % 3 == 0 and not x % 5 == 0:
        string = string + ' Three'
    elif x % 5 == 0 and not x % 3 == 0:
        string = string + ' Five'
    elif x % 5 == 0 and x % 3 == 0:
        string = string + ' Bingo'
    else: string = string + str(f' {x}')
print(string)
