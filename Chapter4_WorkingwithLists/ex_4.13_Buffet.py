# Try It Yourself
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the
# change.
# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

food = ('chicken', 'wings', 'pizza', 'dog', 'cat')
for i in food:
    print(i)

food = ('chicken', 'wings', 'pizza', 'animal', 'snail')
for  x in food:
    print(x)