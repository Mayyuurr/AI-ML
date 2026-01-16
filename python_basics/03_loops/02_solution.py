n= int(input("num:- "))
sum=0

for i in range (0, n+1):
    if i%2==0:
        print(i)
        sum+=i

print("sum upto is", sum)