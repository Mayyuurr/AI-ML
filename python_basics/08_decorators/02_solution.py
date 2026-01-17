def debug(func):
    def wrapper(*args, **kwargs):
        arg_value=', '.join(str(arg) for arg in args)
        kwarg_value=', '.join(str(kwarg) for kwarg in kwargs)
        print(f"Calling :  {func.__name__} , args: {arg_value}, kwargs: {kwarg_value}")
        return func(*args, **kwargs)
    return wrapper


@debug
def hello():
    print("Hey!")

@debug
def greetings(name,greeting="Hello "):
    print(f"{greeting}, {name}")

hello()
greetings("mayyy", "Morning")