def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

# print(even_generator(14)) --return object address

for num in even_generator(10):
    print(num)