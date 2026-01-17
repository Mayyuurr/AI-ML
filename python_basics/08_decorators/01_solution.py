import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} took {round(end-start,3)} sec")
        return result
    return wrapper

@timer
def example_func(n):
    time.sleep(n)

example_func(2)