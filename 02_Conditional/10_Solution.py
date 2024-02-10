pet = input("For Which Animal 'cat' or 'dog': ").capitalize()

age = int(input("Enter a age: "))

if pet == 'Cat':
    if age < 5:
        print('Cat Food')
    else:
        print('Senior Cat Food')

else:
    if age < 3:
        print('Puyppy Food')
    else:
        print('Senior Dog Food')
