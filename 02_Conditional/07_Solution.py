order = str(input("Enter Coffee Size - 'Small', 'Medium', 'Large':")).capitalize()
extra_shot = True

if extra_shot:
    print(f'{order} Coffee with Extra Shot')
else:
    print(f'{order} Coffee')