age=int(input("Enter your age:- "))

day_of_week=(input("Enter the day of the week:- "))


# if (age<18):
#     ticket_price=8
# else:
#     ticket_price=12

ticket_price=12 if age>=18 else 8

if (day_of_week=="Wed"):
    ticket_price-=2
    print("price of ticket is:- $",ticket_price)
else:
    print("Price of ticket is:- $", ticket_price)
