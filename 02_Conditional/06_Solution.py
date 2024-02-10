Mode = int(input('Enter a Distance will suggest you Mode of Transportation: '))

if Mode <= 3:
    print('Go by walk')
elif Mode <= 15:
    print('Go by Bike')
else:
    print('Go by Car')