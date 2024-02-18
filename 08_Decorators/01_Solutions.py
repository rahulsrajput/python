import time

def timer(func):
    def wrapper(*args, **kwargs):
        
        print(f"args: {args} kwargs: {kwargs}")

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f'{func.__name__} ran in {end - start} time')


    return wrapper


@timer
def example_func(n):
    time.sleep(n)


example_func(2)
