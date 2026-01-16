coffee_size=input("Size of coffee (Small,Medium,Large):-")

extra_shot=(input("Want extra shot of espresso(y/n) :-")).lower()

if extra_shot=="y":
    coffee=coffee_size + " coffee with extra shot of espresso!"
else:
    coffee=coffee_size + "coffee with no espresso!"

print(coffee)