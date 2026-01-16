string=input("Enter string:- ")

for char in string:
    if string.count(char)==1:
        print("Non-repeating char is:-", char)
        break

