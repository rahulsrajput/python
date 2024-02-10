Color = str(input("Enter Banana Color 'Green', 'Yellow', 'Brown': ")).capitalize()


if Color == 'Green':
    print('Banana is Unripe')
elif Color == 'Yellow':
    print('Banana is Ripe')
elif Color == 'Brown':
    print('Banana is Overripe')
else:
    print('enter from given color')