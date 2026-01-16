
age=input("Enter age:- ")
age_in_int=int(age)

if (age_in_int<13):
    print("Child")
elif (age_in_int<20):
    print("Teenager")
elif (age_in_int<60):
    print("adult")
else:
    print("Senior")

