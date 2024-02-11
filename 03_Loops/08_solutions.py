number = 4
is_prime= True


if number > 1:
    for x in range(2 , number):
        if (number % x) == 0:
            is_prime = False
            break


print(is_prime)