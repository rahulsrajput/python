a = int(input('Enter Your Age: '))

if (a <= 13):
    print('Child')
elif (a > 13 and a <= 19):
    print('Teenager')
elif (a > 19 and a <= 59):
    print('Adult')
else:
    print('Senior')