weather = input("Enter Current Weather - 'Sunny', 'Rainy', 'Snowy': ").capitalize()

if weather == 'Sunny':
    print("Go on Walk")
elif weather == 'Rainy':
    print("Read a Book")
elif weather == 'Snowy':
    print('Build a Snowman')
else:
    print('Do whatever You want :)')