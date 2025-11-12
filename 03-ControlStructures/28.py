ciąg = [1, 1, 2, 3, 5]
wart_wyrazu = 0
while wart_wyrazu < 100000:
    a = ciąg[int((len(ciąg))-1)]
    b = ciąg[int((len(ciąg))-2)]
    a = int(a)
    b = int(b)
    wart_wyrazu = a + b
    ciąg.append(wart_wyrazu)

print(*ciąg)


    
     