from math import ceil
number_of_items = int(input("Enter the number of items:"))
items_per_box = int(input("Enter the number of items por box:"))

calculate = ceil(number_of_items / items_per_box)

round = round(calculate)

print(f"For {number_of_items} items, packing {items_per_box} items in each box, you will need {round} boxes.")