def recusive_factorial(number):
    # # factorial=1
    # while(number>0):
    #     # factorial*=number
    #     # number-=1
    #     # recusive_factorial(number)
    # return factorial

    if number==0:
        return 1
    else:
        return number*recusive_factorial(number-1)


print(recusive_factorial(5))
