# Create a 99_bottles.py program and use a for loop and a range() function to print out all the verses of "99 Bottles of Beer."

# 99 bottles of beer on the wall
# 99 bottles of beer
# Take one down, pass it around
# 98 bottles of beer on the wall


for i in range (99, 0, -1):
    print(f'{i} bottles of beer on the wall')
    print(f'{i} bottles of beer')
    print("Take one down, pass it around")
