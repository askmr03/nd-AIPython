manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
print("the code breaks the loop when weight exceeds or reaches the limit")
print("METHOD 1")
items = []
weight = 0

for cargo_name,cargo_number in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print(" breaking loop now")
        break 
    else:
        print(" adding {} ({})".format(cargo_name,cargo_number))
        items.append(cargo_name)
        weight += cargo_number

print("\n Final Weight: {}".format(weight))
print("Final Items: {}".format(items))

'''
the code breaks the loop when weight exceeds or reaches the limit
METHOD 1
current weight: 0
 adding bananas (15)
current weight: 15
 adding mattresses (24)
current weight: 39
 adding dog kennels (42)
current weight: 81
 adding machine (120)
current weight: 201
 breaking loop now
'''



# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\n METHOD 2")
weight = 0
items = []

for cargo_name,cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print(" breaking from the loop now!")
    elif weight + cargo_weight > 100:
        print(" skipping {} ({})".format(cargo_name,cargo_weight))
    else:
        print(" adding {} ({})".format(cargo_name,cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


'''
METHOD 2
current weight: 0
 adding bananas (15)
current weight: 15
 adding mattresses (24)
current weight: 39
 adding dog kennels (42)
current weight: 81
 skipping machine (120)
current weight: 81
 adding cheeses (5)

Final Weight: 86
Final Items: ['bananas', 'mattresses', 'dog kennels', 'cheeses']
'''