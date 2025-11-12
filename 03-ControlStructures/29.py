string = ''
n = 2
for x in range(2,10000):
    while n <= x:
        reszta = x % n
        if reszta == 0:
            break 
        else:
            n = n + 1
        if n == x:
            print(x)
    n = 2
        

        




print(string)


        