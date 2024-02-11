n = int(input('enter a number: '))

if n > 0:
    for x in range(1, n+1):
        if x == 5:
            continue
        else:
            print(f'{n} * {x} = {n*x}')