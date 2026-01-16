year=int(input("year to check:- "))

if (year%400==0) or (year%4==0 and year%100!=0):
    print("leap year")
else:
    print("Non-Leap year")