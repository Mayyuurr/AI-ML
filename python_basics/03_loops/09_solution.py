items = ["apple", "banana", "orange", "apple", "mango"]

# for fruit in items:
#     if items.count(fruit)>1:
#         print(fruit)
#         break

unique_items=set()

for item in items:
    if item in unique_items:
        print("Duplicate: ", item)
        break
    unique_items.add(item)