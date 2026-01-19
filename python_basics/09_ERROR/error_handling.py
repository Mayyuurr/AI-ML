file=open('youtube.txt', 'w')

try:
    file.write("Good morining")
finally:
    file.close()

with open("youtube.txt", 'w') as file:
    file.write("New Good Morning")