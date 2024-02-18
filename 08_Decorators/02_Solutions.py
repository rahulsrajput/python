def debug(func):
    def wrapper(*args, **kwargs):

        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())

        print(f"{func.__name__}: greet with args {args_value} and kwargs {kwargs_value}")
        
        func(*args,**kwargs)

    return wrapper



@debug
def hello():
    print('hello')


@debug
def greeting(name, greets='hello'):
    print(f"{greets}, {name}")


hello()
greeting('rahul', greets='good morning')