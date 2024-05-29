
premium_jelly = 1000000

savings = premium_jelly

if savings >= 1000000:
    print("I'm rich!")

# We use square brackets to make lists []

items_a = ["Guava", "Potato", "674"]
print(items_a)

## Use .append to add elements to the end of a list
positions_a = [4,6,9]
positions_a.append(24)
print(positions_a)

## Use .insert to add values to any part of a list, with (index, element)
# you can only add one value at a time!
positions_a.insert(2, 45)
print(positions_a)

## You can delete values from a list using .pop(index) 
positions_a.pop(3)
print(positions_a)