number_check=int(input("number to check for prime:- "))
is_prime=True

if number_check>1:
    for i in range(2, number_check):
        if number_check%i==0:
            is_prime=False
            break

if is_prime==True:
    print("number is prime")
else:
    print("number is not prime!")