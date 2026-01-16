def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_kwargs(name="shaktiman",power="flight")
print_kwargs(name="Iron man")
print_kwargs(name="shaktiman",power="lazer", enemy="andera")
