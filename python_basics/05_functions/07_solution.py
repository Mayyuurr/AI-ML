def sum_all(*args):
    print(args)
    for i in args:
        print(2*i)
    print("sum of args is: ",sum(args))


sum_all(1,2,3)