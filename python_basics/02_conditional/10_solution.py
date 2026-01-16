pet=input("Enter species of pet:-").lower()

age=int(input("Enter age of pet"))

if pet=="dog":
    if age<2:
        food="puppy food"
    else:
        food="dog food"
elif pet=="cat":
    if age>5:
        food="Senior cat food"
    else:
        food="Cat food"
else:
    food="fav food"

print(pet, "eats", food)