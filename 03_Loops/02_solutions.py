a = int(input('Enter a Number:'))
sum = 0

for x in range(1 , a+1):
    if x % 2 == 0:
        sum = sum + x
print(sum)