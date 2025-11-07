###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
for x in range(1,10):
    if not x%2 ==0:
        continue
    else:
        print(f'1/{x} = {1/x}')