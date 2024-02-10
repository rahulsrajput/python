age = int(input('Enter Your age: '))

Wednesday = True

price = 12 if age >= 18 else 8

if (Wednesday):
    price = price - 2
    print(f'After discount Your Ticket Price is ${price}')
else:
    print(f'Your Ticket Price is ${price}')
    