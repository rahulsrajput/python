def sum_all(*args):

    print(args) #Tuple format ata hai args mai

    for i in args:
        print(i * 2)

    return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,6,7))


# *args = numbers of arguments