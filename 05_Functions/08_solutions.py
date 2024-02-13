def print_kwargs(**kwargs):
    print(kwargs)
    for key , value in kwargs.items():
        print(f"{key} {value}")

print_kwargs(name='rahul',power='lazer')
print_kwargs(name='rahul')
print_kwargs(name='rahul',power='lazer', surname='singh')

