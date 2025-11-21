categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
counter = 0
y = 0
ostatni_counter = 0
while counter < len(expenses):
    if expenses[counter] > y:
        y = expenses[counter]
        ostatni_counter = counter
        counter = counter + 1
    else:
        counter = counter + 1
    
najwiekrze = f'{categories[ostatni_counter]} - {expenses[ostatni_counter]}'

print(najwiekrze)
